#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree, PixelRange
from colorzero import Color
from time import sleep
from random import choice

colors = [Color('red'), Color('green'), Color('blue'), Color('purple'), Color('orange'), Color('navy')]

class Pattern(PatternInterface):
    def apply(self, tree, thread):
        tree.value = [choice(colors) for i in PixelRange.ALL]
        sleep(0.5)
        tree.off()
        sleep(0.5)

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            tree.value = [choice(colors) for i in PixelRange.ALL]
            sleep(0.5)
            tree.off()
            sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
