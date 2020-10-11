import sys
import time
import pytest
import glassOS
from demo_opts import get_device

def test_nothing():
    assert True

def test_displayText():
    try:
        glassOS.device = get_device()
        glassOS.displayText("pineapple")
        assert True, "display said pineapple"
    except Exception as e:
        assert False, "{}: {}".format(type(e),e)

def test_appUpdateTime():
    glassOS.device = get_device()
    glassOS.init()
    for app in glassOS.appNames:
        curApp = glassOS.apps[app]
        curApp.device = glassOS.device
        curApp.init()
        startTime = time.time()
        curApp.update()
        runTime = time.time() - startTime
        assert runTime < 5, app + ".py's update() ran too slow"
