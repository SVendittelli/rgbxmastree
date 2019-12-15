#!/usr/bin/python3

from tree import RGBXmasTree, PixelRange
from colorzero import Color
from random import choice

steps = 100
colors = [Color('red'), Color('green'), Color('blue')]
num_colors = len(colors)

def grad(tree):
    """Generate an array of random color gradients to cycle through. Leaving the star gold."""

    pixel_gradients = [[Color('gold')] * steps] * len(tree)
    for i in PixelRange.NOT_STAR:
        old_color = tree[i].color
        new_color = choice(colors)
        pixel_gradients[i] = list(old_color.gradient(new_color, steps=steps))
    return [*zip(*pixel_gradients)] # transpose

if __name__ == '__main__':
    tree = RGBXmasTree()

    try:
        while True:
            for value in grad(tree):
                tree.value = value
    except (KeyboardInterrupt, SystemExit):
        tree.off()
