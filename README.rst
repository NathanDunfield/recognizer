A barebones and hackish Python interface for Matveev and company's
Spine_, aka The 3-manifold Recognizer.  Specifically, it lets one use
Spine's recognize feature progammatically from Python by driving the
Windows GUI using pywinauto_.  As with Spine itself, this Python module
is only tested on Windows.  It might be possible to adapt this for use
on Linux or macOS via WINE_, but who knows.  

Install into any Windows version of Python via the following command
in this directory::

  python -m pip install .

and then look at the ``test.py`` script for some usage examples. 

Note: The Python module includes its own copy of the Spine binary, so there's
no need to install it directly. 

.. _Spine: http://www.matlas.math.csu.ru/?page=recognizer
.. _pywinauto: http://pywinauto.readthedocs.io/
.. _WINE: https://www.winehq.org/
