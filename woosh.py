#!/usr/bin/python3

from tree import RGBXmasTree, PixelRange
from colorzero import Color
from time import sleep
import random

blue = Color('blue')
colors = [blue] * 1000
colors.append(Color('red'))

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            tree.set_range(PixelRange.BOTTOM, blue)
            sleep(0.1)
            tree.set_range(PixelRange.MIDDLE, blue)
            sleep(0.1)
            tree.set_range(PixelRange.TOP, blue)
            sleep(0.1)
            tree.set_range(PixelRange.STAR, random.choice(colors))
            sleep(0.1)
            tree.off()
            sleep(random.uniform(0.1, 2))
    except (KeyboardInterrupt, SystemExit):
        tree.off()
