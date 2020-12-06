#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree
from colorzero import Color, Hue

class Pattern(PatternInterface):
    def apply(self, tree, thread):
        tree.color = Color('red')
        for _ in range(360):
            if (thread.stopped()):
                break
            tree.color += Hue(deg=1)

if __name__ == '__main__':
    tree = RGBXmasTree()
    tree.color = Color('red')
    try:
        while True:
            tree.color += Hue(deg=1)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
