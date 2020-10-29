import os
import sys
sys.path.append('apps')
import time
import random
import keyboard
from demo_opts import get_device
from luma.core.render import canvas

global running
global appNames
global apps
global curApp
global changedApp
global backupDevice
changedApp = True

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
    keyboard.add_hotkey('space', lambda:onEscape())
    
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
    for entry in os.listdir(path='apps'):
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

def runApp(appName):
    apps[appName].device = device
    apps[appName].init()
    while(running):
        apps[appName].update()

def nextApp():
    global curApp
    global changedApp
    if not running:
        curApp = (curApp + 1)%len(appNames)
        changedApp = True    

def previousApp():
    global curApp
    global changedApp
    if not running:
        curApp -= 1
        if curApp < 0:
            curApp = len(appNames) - 1
        changedApp = True
    
def playCurrent():
    global curApp
    global changedApp
    
    if changedApp:
        appName = appNames[curApp]
        resetDisplay()
        displayText(appName)
        changedApp = False
    elif (running):
        appName = appNames[curApp]
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
    global changedApp
    global device
    if not changedApp:
        running = False
        device.clear()
        displayText("Closing...")
        changedApp = True
    
def resetDisplay():
    global device
    device.cleanup()
    device = get_device()
    
if __name__ == "__main__":
    device = get_device()
    init()
    while True:
        main()
