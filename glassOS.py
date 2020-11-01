import os as linux
import sys
sys.path.append('apps')
import time
import random
import keyboard
from demo_opts import get_device
from luma.core.render import canvas

class OS:
    changedApp = True
    
    def __init__(os, device):
        os.device = device
        os.startUp()
        
    def startUp(os):
        os.importApps()
        os.appNames = os.getApps()
        os.apps = sys.modules
        os.running = False
        os.curApp = 0
        
        #setup input
        keyboard.on_press_key("left", lambda _:previousApp())
        keyboard.on_press_key("right", lambda _:nextApp())
        keyboard.on_press_key("esc", lambda _:onEscape())
        keyboard.on_press_key("enter", lambda _:onEnter())
        keyboard.add_hotkey('space', lambda :onEscape())

    def displayText(os,text):
        os.device.clear()
        with canvas(os.device, dither=True) as draw:
            size = draw.textsize(text)
            left = (os.device.width - size[0]) // 2
            top = (os.device.height - size[1]) // 2
            draw.text((left, top), text=text, fill="white")
            
    def importApps(os):
        appNames = os.getApps()
        appNames.sort()
        for appName in appNames:
            try:
                print("Importing: " + appName)
                __import__(appName, locals(), globals())
            except:
                print("import of app: ." + appName + ". FAILED")
                
    def getApps(os):
        appNames = []
        for entry in linux.listdir(path='apps'):
            if (entry.endswith(".py")
            and(not entry.startswith("camera")
            and entry != "glassOS.py"
            and entry != 'app.py'
            and entry != 'demo_opts.py')):
                appNames.append(entry[:-3])
        return appNames

    def runAnApp(os,appName):
        apps[appName].device = device
        apps[appName].init()
        while(running):
            apps[appName].update()

    def nextApp(os):
        if not running:
            curApp = (curApp + 1)%len(appNames)
            changedApp = True    

    def previousApp(os):
        if not running:
            curApp -= 1
            if curApp < 0:
                curApp = len(appNames) - 1
            changedApp = True
        
    def playCurrentApp(os):
        if changedApp:
            appName = appNames[curApp]
            resetDisplay()
            displayText(appName)
            changedApp = False
        elif (running):
            appName = appNames[curApp]
            apps[appName].update()

    def onEnter(os):
        appName = appNames[curApp]
        apps[appName].device = device
        apps[appName].init()
        running = True

    def onEscape(os):
        if not changedApp:
            running = False
            device.clear()
            displayText("Closing...")
            changedApp = True
        
    def resetDisplay(os):
        device.cleanup()
        device = get_device()
    
if __name__ == "__main__":
    device = get_device()
    os = OS(device)
    print(os)
    os.startUp()
    while True:
        os.main()
