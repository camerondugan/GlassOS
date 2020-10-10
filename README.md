# Smart GlassOS
A python + luma.oled base OS for smart glasses with an ssd1331 oled display on raspberry pi

## Setup on Windows
+ press windows + r
+ type cmd
+ type python
+ Windows store for python should open, click install
+ Clone this repository with git bash or github desktop and open the folder in file explorer
+ Open the Windows folder and double click get-pip.py to install pip for python
	+ If this doesn't work, you can also get it from https://bootstrap.pypa.io/get-pip.py
+ Go back to cmd and type ```pip install lxml bs4 requests pygame luma.oled luma.emulator keyboard```
+ to run the os go to this folder in cmd and run ```python glassOS.py -d pygame --width 96 --height 64```

## Setup Linux Debian/Ubuntu+
+ Update your computer: ```sudo apt update && sudo apt upgrade```
+ Clone over https into a folder where you will remember it
+ Install python3 and python3-pip: ```sudo apt install python3 python3-pip```
+ Install extra dependencies ```sudo apt install python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y```
+ Install app dependencies ```sudo pip3 intall lxml bs4 requests```
+ Install keyboard for super user in python3: ```sudo pip3 install keyboard```
+ Install Luma for super user also in python3: ```sudo -H pip3 install luma.oled```

## Running The OS
+ Open the folder in a terminal
+ Required to run on the display with the pi: ```sudo usermod -a -G spi,gpio,i2c $USER```
+ To run on hardware:
	+ ```sudo python3 glassOS.py -i spi -d ssd1331 --width 96 --height 64```

## Emulating The OS
+ Open the folder in a terminal
+ Required to emulation: ```sudo pip3 install luma.emulator```
+ To emulate:
	+ ```sudo python3 glassOS.py -i spi -d pygame --width 96 --height 64```

## Using the OS
+ arrow keys to switch apps
+ enter key to enter
+ press the escape key to exit
+ If you are running the elumator use ctrl+1 to exit

## DIY Python App Requirements
+ an init() method and an update() method
+ the update() method should only take about 1-2 seconds per cycle
+ your python app is in the same folder as the glassOS.py file
+ In the Broken or Rejected folder there is a demo.py that you can look to for the basic functions
