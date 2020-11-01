import sys
import time
import pytest
import glassOS
from demo_opts import get_device

def test_nothing():
    assert True

def test_startUp():
    try:
        os = glassOS.OS(get_device())
        os.startUp()
        assert (not os.running
                and os.curApp == 0
                and os.count == 0), "OS started up, but some variables are wrong"
    except Exception as e:
        assert False, "{}: {}".format(type(e),e)

def test_displayText():
    try:
        os = glassOS.OS(get_device())
        os.displayText("pineapple")
        assert True, "display said pineapple"
    except Exception as e:
        assert False, "{}: {}".format(type(e),e)

def test_previousApp():
    try:
        os = glassOS.OS(get_device())
        os.nextApp()
        assert True, "displayed the previous app"
    except Exception as e:
        assert False, "{}: {}".format(type(e),e)

def test_nextApp():
    try:
        os = glassOS.OS(get_device())
        os.nextApp()
        assert True, "displayed the next app"
    except Exception as e:
        assert False, "{}: {}".format(type(e),e)

def test_getApps():
    try:
        os = glassOS.OS(get_device())
        apps = os.getApps()
        assert (len(apps) > 0), "found no glassOS apps in the apps folder"
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
        assert runTime < 5, app + ".py's update() function took more than 5 seconds to run"
