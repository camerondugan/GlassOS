#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Greyscale rendering demo.
"""

import time
import os.path
from demo_opts import get_device
from luma.core.render import canvas
from PIL import Image

global img_path
global balloon
global mode

def init():
    global balloon
    global img_path
    global mode
    global startTime
    
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'images', 'balloon.png'))
    balloon = Image.open(img_path) \
        .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
        .convert("L") \
        .convert(device.mode)
    mode = 0
    startTime = time.time()

def update():
    global balloon
    global img_path
    global mode
    global startTime
    
    if (mode == 0):
        # Image display
        device.display(balloon)
        device.display(balloon)

    if (mode == 1):
        # Greyscale
        shades = 16
        w = device.width / shades
        for _ in range(2):
            with canvas(device, dither=True) as draw:
                for i, color in enumerate(range(0, 256, shades)):
                    rgb = (color << 16) | (color << 8) | color
                    draw.rectangle((i * w, 0, (i + 1) * w, device.height), fill=rgb)
    
                size = draw.textsize("greyscale")
                left = (device.width - size[0]) // 2
                top = (device.height - size[1]) // 2
                right = left + size[0]
                bottom = top + size[1]
                draw.rectangle((left - 1, top, right, bottom), fill="black")
                draw.rectangle(device.bounding_box, outline="white")
                draw.text((left, top), text="greyscale", fill="white")
    mode = time.time() - startTime
    mode %= 2

if __name__ == "__main__":
    try:
        device = get_device()
        init()
        while True:
            update()
    except KeyboardInterrupt:
        pass
