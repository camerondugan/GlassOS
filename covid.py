import os
import lxml
import time
import requests
from PIL import ImageFont
from PIL import ImageDraw
from bs4 import BeautifulSoup
from demo_opts import get_device
from luma.core.virtual import terminal

global term
global covidCases
global refreshInMin
global startTime
global covidCode

def init():
    global term
    global covidCases
    global refreshInMin
    global startTime
    term = terminal(device, make_font("pixelmix.ttf",12))
    term.println("Loading...")
    covidCases = getCovidCases()
    global covidCode
    covidCode = getCovidCode()
    refreshInMin = 10
    startTime = time.time()

def update():
    global term
    global covidCases
    global covidCode
    global refreshInMin
    global startTime
    runTime = time.time()-startTime
    if (round(runTime) / (refreshInMin*60) >= 1):
        covidCases = getCovidCases()
        startTime = time.time()
    if (round(runTime) / (refreshInMin*60) >= 1):
        covidCode = getCovidCode()
        startTime = time.time()
    term.println(covidCases + " cases at")
    term.println("Wentworth")
    term.println(covidCode)
    time.sleep(1)
    
def getCovidCases():
    source = requests.get('https://wit.edu/re-entry/dashboard').text
    soup = BeautifulSoup(source, 'lxml')
    testData = soup.find('body')
    covidCases = testData.find('article', class_='node node-covid-dashboard view-mode-full')
    covidCases = covidCases.findAll('div', class_='row dashboard-wrapper')[3]
    covidCases = covidCases.findAll('div', class_='columns medium-6 small-12')[1].div.div.div
    return covidCases.text

def getCovidCode():
    source = requests.get('https://wit.edu/re-entry/dashboard').text
    soup = BeautifulSoup(source, 'lxml')
    testData = soup.find('body')
    covidCode = testData.find('div', class_='page')
    covidCode = covidCode.find('div', class_='off-canvas-wrap')
    covidCode = covidCode.find('div', class_='inner-wrap').main
    covidCode = covidCode.find('div', class_='medium-9 main columns').article
    covidCode = covidCode.find('div', class_='row dashboard-wrapper')
    covidCode = covidCode.findAll('div')[1]
    covidCode = covidCode.find('div', class_='columns medium-9 small-12').div.div.div
    return covidCode.text

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

if __name__ == "__main__":
    try:
        device = get_device()
        init()
        while True:
            update()
    except KeyboardInterrupt:
        pass

