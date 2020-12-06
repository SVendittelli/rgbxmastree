#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree, PixelRange
from colorzero import Color

colors = [Color('red'), Color('green'), Color('blue')]

class Pattern(PatternInterface):
    def run(tree):
        tree.set_range(PixelRange.STAR, Color('gold'))
        num_colors = len(colors)
        for i in range(num_colors):
            for col in colors[i].gradient(colors[(i+1) % num_colors], steps=100):
                tree.set_range(PixelRange.NOT_STAR, col)

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        tree.set_range(PixelRange.STAR, Color('gold'))
        num_colors = len(colors)
        while True:
            for i in range(num_colors):
                for col in colors[i].gradient(colors[(i+1) % num_colors], steps=100):
                    tree.set_range(PixelRange.NOT_STAR, col)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
