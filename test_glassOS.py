import sys
import pytest
import glassOS
from demo_opts import get_device

def test_nothing():
    assert True == True

def test_displayText():
    glassOS.device = get_device()
    glassOS.displayText("pineapple")
    answer = input("What does the display say? ")
    assert answer == "pineapple", "displayText() failed"
