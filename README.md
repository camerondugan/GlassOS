# Smart GlassOS

A python + luma.oled base OS for smart glasses

## Setup Linux Debian/Ubuntu+
+ Update your computer: ```sudo apt update && sudo apt upgrade```
+ Install python3 and python3-pip: ```sudo apt install python3 python3-pip```
+ Install Extra dependencies ```sudo apt install python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y'''
+ Install keyboard for super user in python3: ```sudo pip3 install keyboard```
+ Install Luma for super user also in python3: ```sudo -H pip3 install luma.oled```

## App Requirements
+ an init() method and an update()  method
+ the update() method should only take about 1-2 seconds per cycle
+ your python app is in the same folder as the glassOS.py file

