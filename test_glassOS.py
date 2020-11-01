import sys
import time
import pytest
import glassOS
from demo_opts import get_device

def test_nothing():
    assert True

def test_displayText():
    try:
        os = glassOS.OS(get_device())
        os.displayText("pineapple")
        assert True, "display said pineapple"
    except Exception as e:
        assert False, "{}: {}".format(type(e),e)

def test_appUpdateTime():
    os = glassOS.OS(get_device())
    os.startUp()
    for app in os.appNames:
        curApp = os.apps[app]
        curApp.device = os.device
        curApp.init()
        startTime = time.time()
        curApp.update()
        runTime = time.time() - startTime
        assert runTime < 5, app + ".py's update() ran too slow"
