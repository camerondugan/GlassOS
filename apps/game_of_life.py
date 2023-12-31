#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Conway's game of life.

Adapted from:
http://codereview.stackexchange.com/a/108121
"""

import time
from random import randint
from demo_opts import get_device
from luma.core.render import canvas


def neighbors(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def iterate(board):
    new_board = set([])
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

global scale
global cols
global rows
global initial_population
global i

def draw(board):
    global i
    with canvas(device, dither=True) as draw:
        for x, y in board:
            left = x * scale
            top = y * scale
            if scale == 1:
                draw.point((left, top), fill="white")
            else:
                right = left + scale
                bottom = top + scale
                draw.rectangle((left, top, right, bottom), fill="white", outline="black")
    if i >= 500:
        init()
        i -= 1
    i += 1

def init():
    global scale
    global cols
    global rows
    global initial_population
    global i
    global board
    i = 0
    scale = 3
    cols = device.width // scale
    rows = device.height // scale
    initial_population = int(cols * rows * 0.33)
    board = set((randint(0, cols), randint(0, rows)) for _ in range(initial_population))
    with canvas(device, dither=True) as draws:
        w, h = draws.textsize("Game of Life")
        left = (device.width - w) // 2
        top = (device.height - h) // 2
        draws.rectangle((left - 1, top, left + w + 1, top + h), fill="black", outline="white")
        draws.text((left + 1, top), text="Game of Life", fill="white")
    time.sleep(3)

def update():
    global board
    global scale
    global cols
    global rows
    global initial_population
    
    draw(board)
    board = iterate(board)


if __name__ == "__main__":
    try:
        device = get_device()
        init()
        while True:
            update()
    except KeyboardInterrupt:
        pass
