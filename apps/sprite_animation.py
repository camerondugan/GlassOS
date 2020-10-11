#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Sprite animation
"""

import time
import os.path
from demo_opts import get_device
from PIL import Image

global image_path
global spritemap
global background
global w
global h
global scale
global new_size
global frame

def update():
    global image_path
    global spritemap
    global background
    global w
    global h
    global scale
    global new_size
    global frame

    x = w * (frame % 8)
    y = h * (frame // 8)
    img = spritemap.crop((x, y, x + w, y + h)).resize(new_size)
    offset = (device.width - img.width) // 2
    background.paste(img, (offset, 0))
    device.display(background.convert(device.mode))
    frame += 1
    frame = frame % 40
    time.sleep(0.05)

def init():
    global image_path
    global spritemap
    global background
    global w
    global h
    global scale
    global new_size
    global frame

    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'images', 'mickey-sprite.png'))
    spritemap = Image.open(img_path).convert("RGBA")

    background = Image.new("RGBA", device.size, "black")

    w = 256
    h = 308
    scale = device.height / float(h)
    new_size = (int(scale * w), device.height)
    frame = 0

if __name__ == "__main__":
    try:
        device = get_device()
        init()
        while True:
            update()
    except KeyboardInterrupt:
        pass
