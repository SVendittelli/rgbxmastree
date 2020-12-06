from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree
from colorzero import Hue
from random import random

def random_color():
    r = random()
    g = random()
    b = random()
    return (r, g, b)

def random_colors(n):
    return [random_color() for i in range(n)]

class Pattern(PatternInterface):
    def apply(self, tree, thread):
        tree.value = random_colors(25)

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            tree.value = random_colors(25)
    except (KeyboardInterrupt, SystemExit):
        tree.off()
