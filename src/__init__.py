"""
Run Matveev and companies Spine, aka The 3-manifold Recognizer,
progammatically by driving the Windows GUI using pywinauto.
"""

import pywinauto
from . import gui
import os, sys

binary_path = os.path.join(gui.__path__[0], 'Recognizer.exe')

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
        self.app.wait_cpu_usage_lower(threshold=5, timeout=60)
        ans = edit.text_block().replace('\r', '').split('\n\n')[-1]
        expected = 'Manifold is\n'
        if ans.startswith(expected):
            return ans[len(expected):]
        
        
    
