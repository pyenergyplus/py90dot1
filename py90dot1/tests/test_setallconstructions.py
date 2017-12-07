"""py.test for setallconstructions.py"""

from py90dot1 import setallconstructions


def test_surfacefilter():
    """py.test for surfacefilter"""
    result = setallconstructions.surfacefilter()
    assert result == 2
