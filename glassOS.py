import os
import sys
import time
import random
import keyboard
from demo_opts import get_device
from luma.core.render import canvas

global running
global app_names
global apps
global curApp
global switched
global backupDevice
switched = True

def init():
    global appNames
    global apps
    global running
    global curApp
    
    importApps()
    appNames = getApps()
    apps = sys.modules
    running = False
    curApp = 0
    
    #setup input
    keyboard.on_press_key("left", lambda _:previousApp())
    keyboard.on_press_key("right", lambda _:nextApp())
    keyboard.on_press_key("esc", lambda _:onEscape())
    keyboard.on_press_key("enter", lambda _:onEnter())
    
def main():
    global appNames
    global apps
    
    playCurrent()

def displayText(text):
    global device
    
    device.clear()
    with canvas(device, dither=True) as draw:
        size = draw.textsize(text)
        left = (device.width - size[0]) // 2
        top = (device.height - size[1]) // 2
        draw.text((left, top), text=text, fill="white")

def getApps():
    appNames = []
    for entry in os.listdir():
        if (entry.endswith(".py")
        and(not entry.startswith("camera")
        and entry != "glassOS.py"
        and entry != 'app.py'
        and entry != 'demo_opts.py')):
            appNames.append(entry[:-3])
    return appNames

def importApps():
    appNames = getApps()
    appNames.sort()
    for appName in appNames:
        try:
            print("Importing: " + appName)
            __import__(appName, locals(), globals())
        except:
            print("import of app: ." + appName + ". FAILED")

def nextApp():
    global curApp
    global switched
    if not running:
        curApp = (curApp + 1)%len(appNames)
        switched = True    

def previousApp():
    global curApp
    global switched
    if not running:
        curApp -= 1
        if curApp < 0:
            curApp = len(appNames) - 1
        switched = True
    
def playCurrent():
    global curApp
    global switched
    
    appName = appNames[curApp]
    if switched:
        appName = appNames[curApp]
        resetDisplay()
        displayText(appName)
        switched = False
    elif (running):
        apps[appName].update()
    

def onEnter():
    global curApp
    global running
    global device
    
    appName = appNames[curApp]
    apps[appName].device = device
    apps[appName].init()
    running = True

def onEscape():
    global running
    global switched
    global device
    if not switched:
        running = False
        device.clear()
        displayText("Closing...")
        switched = True
    
def playAll():
    random.shuffle(appNames)
    for appName in appNames:
        count = 0
        apps[appName].device = device
        apps[appName].init()
        displayText(appName.capitalize())
        time.sleep(1.8)
        start = time.time()
        print("Running: " + appName)
        while (time.time() - start < 5):
            apps[appName].update()
        print("Closed: " + appName)
        resetDisplay()

def resetDisplay():
    global device
    device.cleanup()
    device = get_device()
    
if __name__ == "__main__":
    device = get_device()
    init()
    while True:
        main()
