# Smart GlassOS

A python + luma.oled base OS for smart glasses

## Setup Linux Debian/Ubuntu+
+ Update your computer: ```sudo apt update && sudo apt upgrade```
+ Install python3 and python3-pip: ```sudo apt install python3 python3-pip```
+ Install extra dependencies ```sudo apt install python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y```
+ Install keyboard for super user in python3: ```sudo pip3 install keyboard```
+ Install Luma for super user also in python3: ```sudo -H pip3 install luma.oled```
+ Required to Run on an spi/ic2 display: ```sudo usermod -a -G spi,gpio,i2c $USER```
+ Required to emulato: ```sudo pip3 install luma.emulator```

## Running The OS

## DIY Python App Requirements
+ an init() method and an update() method
+ the update() method should only take about 1-2 seconds per cycle
+ your python app is in the same folder as the glassOS.py file
+ In the Broken or Rejected folder there is a demo.py that you can look to for the basic functions
