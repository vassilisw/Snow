#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2007,2008,2010 One Laptop per Child Association, Inc.
# Written by C. Scott Ananian <cscott@laptop.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# pippy sample "snow"

import pippy
import pygame
import sys
from pygame.locals import *
from random import *

# always need to init first thing
pygame.init()

# create the window and keep track of the surface
# for drawing into
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# ask for screen's width and height
width, height = screen.get_size()

# turn off the cursor
pygame.mouse.set_visible(False)

bg_color = (0, 0, 0)

xs = []
ys = []
dxs = []
dys = []
sizes = []
nflakes = 1000

while pippy.pygame.next_frame():
    # if we don't have enough flakes, add one
    if len(xs) < nflakes:
        xs.append(randint(0, width))
        ys.append(0)
        dxs.append(randint(-2, 2))
        size = expovariate(1) * 5
        sizes.append(int(size))
        dys.append(size * 2)

    # clear the screen
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()

    for x, y, size in zip(xs, ys, sizes):
        c = 40 + int(float(y) / height * 215)
        pygame.draw.circle(
            screen, (c, c, c), (x, y), size)

    xs_ = []
    ys_ = []
    dxs_ = []
    dys_ = []
    sizes_ = []

    for x, y, dx, dy, size in zip(xs, ys, dxs, dys, sizes):
        if 0 <= x + dx <= width and 0 <= y + dy <= height:
            xs_.append(x + dx)
            ys_.append(y + int(dy))
            dxs_.append(dx)
            dys_.append(dy)
            sizes_.append(size)

    xs = xs_
    ys = ys_
    dxs = dxs_
    dys = dys_
    sizes = sizes_

    pygame.display.flip()
