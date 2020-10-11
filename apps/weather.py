#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
3 Day weather forecast from the BBC
"""

import sys
import time
import os

from PIL import ImageFont
from demo_opts import get_device
from luma.core.virtual import terminal
from luma.core.legacy.font import proportional, SINCLAIR_FONT

try:
    import feedparser
except ImportError:
    print("The feedparser library was not found. Run 'sudo -H pip install feedparser' to install it.")
    sys.exit()

global location_id
global weather_rss_url
global device
global term
global i
global im
global feed

def init():
    global weather_rss_url
    global location_id
    global device
    global term
    global i
    global im
    global feed
    location_id = 4930956
    weather_rss_url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/{}".format(location_id)
    device = get_device()
    i = 0
    im = 0
    font = make_font("miscfs_.ttf",10)
    term = terminal(device, font)
    feed = feedparser.parse(weather_rss_url)
    msg = feed["feed"]["title"]
    term.puts(msg)
    term.newline()
    time.sleep(1)


def update():
    # Go to http://www.bbc.co.uk/weather and enter your town/city into
    # the 'Find a forecast' box. Then when you click through, substitute
    # the location_id below
    global weather_rss_url
    global location_id
    global device
    global term
    global i
    global im
    global feed

    #print("{}: {}".format(i,(i+1)%3))
    items = feed["items"][i]
    i = (i + 1) % (3)
    msg = items["title"]
    msg = msg.split(",")[0]
    term.puts(msg)
    term.newline()

    #print("{}: {}".format(im,(im+1)%3))
    msg = items["description"].split(",")[im]
    im = (im + 1) % 3
    term.puts(msg)
    term.newline()
    time.sleep(2)

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

if __name__ == "__main__":
    init()
    while True:
        update()
