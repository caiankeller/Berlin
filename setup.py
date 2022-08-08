from setuptools import setup

APP = ['Berlin.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': "berlin.jpg",
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name="Berlin",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
