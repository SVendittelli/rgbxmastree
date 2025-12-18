from colorzero import Color


def subtract(list1: list, list2: list):
    """Remove all the items that appear in list2 from list1"""
    return [x for x in list1 if x not in list2]


class PixelRange:
    """Ranges of lights on the tree"""

    ALL = list(range(25))

    STAR = [3]
    TOP = [2, 18, 13, 4, 10, 22, 21, 9]
    MIDDLE = [1, 17, 14, 5, 11, 23, 20, 8]
    BOTTOM = [0, 16, 15, 6, 12, 24, 19, 7]

    FRONT = [0, 1, 2, 4, 5, 6]
    BACK = [7, 8, 9, 10, 11, 12]
    LEFT = [13, 14, 15, 22, 23, 24]
    RIGHT = [16, 17, 18, 19, 20, 21]

    NOT_STAR = subtract(ALL, STAR)

    FRONT_BRANCH = [13, 14, 15, 16, 17, 18]
    BACK_BRANCH = [19, 20, 21, 22, 23, 24]
    LEFT_BRANCH = [4, 5, 6, 10, 11, 12]
    RIGHT_BRANCH = [0, 1, 2, 7, 8, 9]

    FRONT_SIDE = subtract(FRONT, FRONT_BRANCH)
    BACK_SIDE = subtract(BACK, BACK_BRANCH)
    LEFT_SIDE = subtract(LEFT, LEFT_BRANCH)
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
