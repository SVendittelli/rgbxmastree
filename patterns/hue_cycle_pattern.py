#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree
from colorzero import Color, Hue

class Pattern(PatternInterface):
    def run(tree):
        pass

if __name__ == '__main__':
    tree = RGBXmasTree()
    tree.color = Color('red')
    try:
        while True:
            tree.color += Hue(deg=1)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
