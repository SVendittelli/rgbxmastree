#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree, PixelRange
from colorzero import Color
from time import sleep
from random import choice

colors = [Color('red'), Color('green'), Color('blue'), Color('purple'), Color('orange'), Color('navy')]

class Pattern(PatternInterface):
    def run(tree):
        pass

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        tree.value = [choice(colors) for i in PixelRange.ALL]
        tree.set_range(PixelRange.STAR, Color('gold'))
        while True:
            tree[choice(PixelRange.NOT_STAR)].color = choice(colors)
            sleep(0.2)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
