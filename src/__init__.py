"""
Run Matveev and companies Spine, aka The 3-manifold Recognizer,
progammatically by driving the Windows GUI using pywinauto.
"""

import pywinauto
from . import gui
import os, sys, io

binary_path = os.path.join(gui.__path__[0], 'Recognizer.exe')


def closed_isosigs(snappy_manifold, tries_per_description=20):
    """
    Generate a slew of 1-vertex triangulations of a closed manifold
    using SnapPy.
    
    >>> M = snappy.Manifold('m004(1,2)')
    >>> len(closed_isosigs(M, trys=5)) > 0
    True
    """
    import snappy
    M = snappy.Manifold(snappy_manifold)
    assert M.cusp_info('complete?') == [False]
    surgery_descriptions = [M.copy()]

    try:
        for curve in M.dual_curves():
            N = M.drill(curve)
            N.dehn_fill((1,0), 1)
            surgery_descriptions.append(N.filled_triangulation([0]))
    except snappy.SnapPeaFatalError:
        pass

    if len(surgery_descriptions) == 1:
        # Try again, but unfill the cusp first to try to find more
        # dual curves.
        try:
            filling = M.cusp_info(0).filling
            N = M.copy()
            N.dehn_fill((0, 0), 0)
            N.randomize()
            for curve in N.dual_curves():
                D = N.drill(curve)
                D.dehn_fill([filling, (1,0)])
                surgery_descriptions.append(D.filled_triangulation([0]))
        except snappy.SnapPeaFatalError:
            pass

    ans = set()
    for N in surgery_descriptions:
        for i in range(tries_per_description):
            T = N.filled_triangulation()
            if T._num_fake_cusps() == 1:
                n = T.num_tetrahedra()
                ans.add((n, T.triangulation_isosig(decorated=False)))
            N.randomize()

    return [iso for n, iso in sorted(ans)]


class Recognizer(object):
    def __init__(self):
        self.app = app = pywinauto.Application(backend='win32')
        app.start(binary_path)

    def __del__(self):
        self.app.kill()

    def recognize(self, data):
        top = self.app.top_window()
        top.menu_select('File -> New')
        self.win = win = self.app.window(title_re="Manifold Recognizer - \[Untitled\d+\]")
        self.edit = edit = pywinauto.controls.win32_controls.EditWrapper(win.RICHEDIT.wrapper_object())
        edit.set_text(data)
        win.menu_select('Recognizer -> Make Default Moves')
        self.app.wait_cpu_usage_lower(threshold=5, timeout=120)
        ans = edit.text_block().replace('\r', '').split('\n\n')[-1]
        expected = 'Manifold is\n'
        if ans.startswith(expected):
            return ans[len(expected):]
        
    def recognize_snappy(self, manifold, tries=1):
        import snappy
        isosigs = closed_isosigs(manifold)
        for iso in isosigs[:tries]:
            T = snappy.snap.t3mlite.Mcomplex(iso)
            buffer = io.StringIO()
            T.save(buffer, format='spine')
            ans = self.recognize(buffer.getvalue())
            if ans is not None:
                return ans

            
            
        
        
