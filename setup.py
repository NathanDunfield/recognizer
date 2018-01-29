long_description =  """
Python interface Matveev and company's Spine, aka The 3-manifold
Recognizer, via scripting the GUI application.
"""

from setuptools import setup, Command

setup(
    name = 'recognizer',
    version = '1.0a1',
    description = '3-manifold recognizer',
    long_description = long_description,
    url = 'https://bitbucket.org/nathan_dunfield/recognizer',
    author = 'Nathan M. Dunfield, Sergei Matveev and others',
    author_email = 'nathan@dunfield.info',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Operating System :: Windows',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],
    packages = ['recognizer', 'recognizer/gui'],
    package_dir = {'recognizer':'src',
                   'recognizer/gui':'gui'},
    package_data = {'recognizer/gui': ['Recognizer.exe']},
    zip_safe = False,
    install_requires = ['pywinauto'],
)

