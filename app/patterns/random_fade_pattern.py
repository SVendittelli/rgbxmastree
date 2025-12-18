import asyncio

from colorzero import Color
from random import choice

from ..pixels import PixelRange

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

class RandomFadePattern:
    def __init__(self, tree):
        self.tree= tree

    async def run(self):
        while True:
            for value in grad(self.tree):
                self.tree.value = value
                await asyncio.sleep(0.1)
