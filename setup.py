import sys

from setuptools import setup

if sys.version_info < (3, 9):
    raise RuntimeError('"steam-community-market" requires Python 3.9+.')

setup()
