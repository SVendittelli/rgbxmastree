#!/usr/bin/python3

from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.color = Color('red')

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            tree.color += Hue(deg=1)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
