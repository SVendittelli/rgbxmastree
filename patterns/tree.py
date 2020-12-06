#!/usr/bin/python3

from gpiozero import SPIDevice, SourceMixin
from colorzero import Color
from statistics import mean
from time import sleep
from copy import deepcopy

def subtract(list1: list, list2: list):
    return [x for x in list1 if x not in list2]

class PixelRange:
    """Ranges of lights on the tree"""

    ALL = list(range(25))

    STAR   = [3]
    TOP    = [2, 18, 13, 4, 10, 22, 21, 9]
    MIDDLE = [1, 17, 14, 5, 11, 23, 20, 8]
    BOTTOM = [0, 16, 15, 6, 12, 24, 19, 7]

    FRONT = [0, 1, 2, 4, 5, 6]
    BACK  = [7, 8, 9, 10, 11, 12]
    LEFT  = [13, 14, 15, 22, 23, 24]
    RIGHT = [16, 17, 18, 19, 20, 21]

    NOT_STAR = subtract(ALL, STAR)

    FRONT_BRANCH = [13, 14, 15, 16, 17, 18]
    BACK_BRANCH  = [19, 20, 21, 22, 23, 24]
    LEFT_BRANCH  = [4, 5, 6, 10, 11, 12]
    RIGHT_BRANCH = [0, 1, 2, 7, 8, 9]

    FRONT_SIDE = subtract(FRONT, FRONT_BRANCH)
    BACK_SIDE  = subtract(BACK, BACK_BRANCH)
    LEFT_SIDE  = subtract(LEFT, LEFT_BRANCH)
    RIGHT_SIDE = subtract(RIGHT, RIGHT_BRANCH)

class Pixel:
    """An individual light on the tree"""

    def __init__(self, parent, index):
        self.parent = parent
        self.index = index

    @property
    def value(self):
        return self.parent.value[self.index]

    @value.setter
    def value(self, value):
        new_parent_value = list(self.parent.value)
        new_parent_value[self.index] = value
        self.parent.value = tuple(new_parent_value)

    @property
    def color(self):
        return Color(*self.value)

    @color.setter
    def color(self, c):
        r, g, b = c
        self.value = (r, g, b)

    def on(self):
        self.value = (1, 1, 1)

    def off(self):
        self.value = (0, 0, 0)


class RGBXmasTree(SourceMixin, SPIDevice):
    """The xmas tree with 25 lights"""

    def __init__(self, pixels=25, brightness=0.1, mosi_pin=12, clock_pin=25, *args, **kwargs):
        """
        Parameters
        ----------
        pixels : int
            The number of lights (default is 25)
        brightness : float
            The brightness of the lights (default is 0.1, min 0, max 1)
        """

        super(RGBXmasTree, self).__init__(mosi_pin=mosi_pin, clock_pin=clock_pin, *args, **kwargs)
        self._all = [Pixel(parent=self, index=i) for i in range(pixels)]
        self._value = [(0, 0, 0)] * pixels
        self.brightness = brightness
        self.off()

    def __len__(self):
        return len(self._all)

    def __getitem__(self, index):
        return self._all[index]

    def __iter__(self):
        return iter(self._all)

    @property
    def color(self):
        average_r = mean(pixel.color[0] for pixel in self)
        average_g = mean(pixel.color[1] for pixel in self)
        average_b = mean(pixel.color[2] for pixel in self)
        return Color(average_r, average_g, average_b)

    @color.setter
    def color(self, c):
        r, g, b = c
        self.value = ((r, g, b),) * len(self)

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        max_brightness = 31
        self._brightness_bits = int(brightness * max_brightness)
        self._brightness = brightness
        self.value = self.value

    @property
    def value(self) -> list:
        return self._value

    @value.setter
    def value(self, value):
        start_of_frame = [0]*4
        end_of_frame = [0]*5
                     # SSSBBBBB (start, brightness)
        brightness = 0b11100000 | self._brightness_bits
        pixels = [[int(255*v) for v in p] for p in value]
        pixels = [[brightness, b, g, r] for r, g, b in pixels]
        pixels = [i for p in pixels for i in p]
        data = start_of_frame + pixels + end_of_frame
        self._spi.transfer(data)
        self._value = value

    def on(self):
        self.value = [(1, 1, 1)] * len(self)

    def off(self):
        self.value = [(0, 0, 0)] * len(self)

    def close(self):
        super(RGBXmasTree, self).close()

    def set_range(self, pixel_range, color):
        """Set a range of pixels to a color simultaneously"""

        temp = self.value.copy()
        for pixel_index in pixel_range:
            r, g, b = color
            temp[pixel_index] = (r, g, b)
        self.value = temp

if __name__ == '__main__':
    tree = RGBXmasTree()
