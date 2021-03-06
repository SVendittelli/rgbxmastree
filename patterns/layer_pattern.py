#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree, PixelRange
from colorzero import Color
from time import sleep

class Pattern(PatternInterface):
    def apply(self, tree, thread):
        tree.set_range(PixelRange.STAR, Color('gold'))
        sleep(0.15)
        tree.set_range(PixelRange.TOP, Color('red'))
        sleep(0.15)
        tree.set_range(PixelRange.MIDDLE, Color('green'))
        sleep(0.15)
        tree.set_range(PixelRange.BOTTOM, Color('blue'))
        sleep(0.5)
        tree.off()
        sleep(0.5)

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            tree.set_range(PixelRange.STAR, Color('gold'))
            sleep(0.15)
            tree.set_range(PixelRange.TOP, Color('red'))
            sleep(0.15)
            tree.set_range(PixelRange.MIDDLE, Color('green'))
            sleep(0.15)
            tree.set_range(PixelRange.BOTTOM, Color('blue'))
            sleep(0.5)
            tree.off()
            sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
