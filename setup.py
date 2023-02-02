"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = [('', ['assets'])]
OPTIONS = {
    'iconfile': 'icon.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    name='CrystalRCM',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)