#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Simple println capabilities.
"""

import os
import time
import random
from demo_opts import get_device
from luma.core.virtual import terminal
from PIL import ImageFont


def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

global fonts

def update():
    global fonts
    random.shuffle(fonts)
    font = make_font(fonts[0],random.randint(1,2)*4)
    fontname = fonts[0]
    term = terminal(device, font)

    term.println("Terminal mode demo")
    term.println("------------------")
    term.println("Uses any font to output text using a number of different print methods.")
    term.println()
    time.sleep(2)
    term.println("The '{0}' font supports a terminal size of {1}x{2} characters.".format(fontname, term.width, term.height))
    term.println()
    time.sleep(2)
    term.println("An animation effect is defaulted to give the appearance of spooling to a teletype device.")
    term.println()
    time.sleep(2)

    term.println("".join(chr(i) for i in range(32, 127)))
    time.sleep(2)

    term.clear()
    for i in range(30):
        term.println("Line {0:03d}".format(i))

    term.animate = False
    time.sleep(2)
    term.clear()

    term.println("Progress bar")
    term.println("------------")
    for mill in range(0, 10001, 25):
        term.puts("\rPercent: {0:0.1f} %".format(mill / 100.0))
        term.flush()

    time.sleep(2)
    term.clear()
    term.puts("Backspace test.")
    term.flush()
    time.sleep(2)
    for _ in range(17):
        term.backspace()
        time.sleep(0.2)

    time.sleep(2)
    term.clear()
    term.animate = True
    term.println("Tabs test")
    term.println("|...|...|...|...|...|")
    term.println("1\t2\t4\t11")
    term.println("992\t43\t9\t12")
    term.println("\t3\t99\t1")
    term.flush()
    time.sleep(2)

def init():
    global fonts
    fonts = ["tiny.ttf","ProggyTinny.ttf","creep.bdf","miscfs_.ttf","FreePixel.ttf", "ChiKareGo.ttf"]

if __name__ == "__main__":
    try:
        device = get_device()
        init()
        while True:
            update()
    except KeyboardInterrupt:
        pass
