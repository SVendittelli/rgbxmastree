#!/usr/bin/python3

from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree, PixelRange
from colorzero import Color
from time import sleep
from random import choice, randrange, uniform
from math import ceil, floor

blue = Color('blue')
red = Color('red')

class Pattern(PatternInterface):
    def apply(self, tree, thread):
        limit = randrange(680, 760) # expected 720 = seconds in 18 minutes / average cycle time for blue (1.5 seconds)
        print('Limit: {}'.format(limit))

        count = 0
        while count < limit and not thread.stopped():
            seconds = ceil((limit - count) * 1.5)
            minutes = floor(seconds / 60)
            print('{:3} / {:3} ({:02}:{:02} approx.)'.format(count + 1, limit, minutes, seconds % 60))
            sleep(uniform(0.1, 2)) # expected 1.1
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

        if (thread.stopped()):
            return

        # flash red 7 times
        for i in range(7):
            sleep(0.25)
            tree.set_range(PixelRange.STAR, red)
            sleep(0.25)
            tree.off()

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            limit = randrange(680, 760) # expected 720 = seconds in 18 minutes / average cycle time for blue (1.5 seconds)
            print('Limit: {}'.format(limit))

            count = 0
            while count < limit:
                seconds = ceil((limit - count) * 1.5)
                minutes = floor(seconds / 60)
                print('{:3} / {:3} ({:02}:{:02} approx.)'.format(count + 1, limit, minutes, seconds % 60))
                sleep(uniform(0.1, 2)) # expected 1.1
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
