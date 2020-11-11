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
        os.updateTheOS()
        
    def startUp(os):
        os.importApps()
        os.appNames = os.getApps()
        os.apps = sys.modules
        os.running = False
        os.curApp = 0
        os.count = 0
        
        #setup input
        keyboard.on_press_key("left", lambda _:os.previousApp())
        keyboard.on_press_key("right", lambda _:os.nextApp())
        keyboard.on_press_key("esc", lambda _:os.onEscape())
        keyboard.on_press_key("enter", lambda _:os.onEnter())
        keyboard.add_hotkey('space', lambda: os.onEscape())

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
            and entry != "glassOS.py"
            and entry != 'app.py'
            and entry != 'demo_opts.py'):
                appNames.append(entry[:-3])
        return appNames

    def runAnApp(os,appName):
        os.apps[appName].device = os.device
        os.apps[appName].init()
        while(os.running):
            os.apps[appName].update()

    def nextApp(os):
        if not os.running:
            os.curApp = (os.curApp + 1)%len(os.appNames)
            os.changedApp = True    

    def previousApp(os):
        if not os.running:
            os.curApp -= 1
            if os.curApp < 0:
                os.curApp = len(os.appNames) - 1
            os.changedApp = True
        
    def update(os):
        if os.changedApp:
            appName = os.appNames[os.curApp]
            os.resetDisplay()
            os.displayText(appName)
            os.changedApp = False
        elif (os.running):
            appName = os.appNames[os.curApp]
            os.apps[appName].update()

    def updateTheOS(os):
        linux.system("sudo -u pi git pull")

    def onEnter(os):
        appName = os.appNames[os.curApp]
        os.apps[appName].device = os.device
        os.apps[appName].init()
        os.running = True

    def onEscape(os):
        if not os.changedApp:
            os.running = False
            os.device.clear()
            os.displayText("Closing...")
            os.changedApp = True
        
    def resetDisplay(os):
        os.device.cleanup()
        os.device = get_device()
    
if __name__ == "__main__":
    device = get_device()
    os = OS(device)
    while True:
        os.update()
