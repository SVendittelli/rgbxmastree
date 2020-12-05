#!/usr/bin/python3

from tree import RGBXmasTree, PixelRange
from colorzero import Color
from random import randrange

steps = 100
colors = [Color('red'), Color('green'), Color('blue')]
num_colors = len(colors)

gradients = [[]] * num_colors
for i in range(num_colors):
    gradients[i] = list(colors[i].gradient(colors[(i+1) % num_colors], steps=steps))

if __name__ == '__main__':
    tree = RGBXmasTree()

    arr = [[Color('gold')] * (num_colors * steps)] * len(tree)
    for i in PixelRange.NOT_STAR:
        arr[i] = []
        for j in range(num_colors):
            arr[i] += gradients[(i+j) % num_colors]
    trans = [*zip(*arr)] # transpose

    try:
        while True:
            for val in trans:
                tree.value = val
    except (KeyboardInterrupt, SystemExit):
        tree.off()
