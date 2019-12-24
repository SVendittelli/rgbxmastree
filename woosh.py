#!/usr/bin/python3

from tree import RGBXmasTree, PixelRange
from colorzero import Color
from time import sleep
from random import choice, randrange, triangular

blue = Color('blue')
red = Color('red')

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            limit = randrange(40, 2200) # expected 1080 (seconds in 18 minutes)
            print('Limit: {}'.format(limit))

            count = 0
            while count < limit:
                sleep(triangular(0.1, 2, 0.6)) # sleep at least 0.1, at most 2, on average 0.6
                tree.set_range(PixelRange.BOTTOM, blue)
                sleep(0.1)
                tree.set_range(PixelRange.MIDDLE, blue)
                sleep(0.1)
                tree.set_range(PixelRange.TOP, blue)
                sleep(0.1)
                tree.set_range(PixelRange.STAR, blue)
                sleep(0.1)
                tree.off()
                count = count + 1

            # flash red 7 times
            for i in range(7):
                sleep(0.25)
                tree.set_range(PixelRange.STAR, red)
                sleep(0.25)
                tree.off()
    except (KeyboardInterrupt, SystemExit):
        tree.off()
