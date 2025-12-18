import asyncio
from random import randrange

from colorzero import Color

from ..pixels import PixelRange

steps = 100
colors = [Color("red"), Color("green"), Color("blue")]
num_colors = len(colors)

gradients = [[]] * num_colors
for i in range(num_colors):
    gradients[i] = list(colors[i].gradient(colors[(i + 1) % num_colors], steps=steps))

arr = [[Color("gold")] * (num_colors * steps)] * 25
for i in PixelRange.NOT_STAR:
    arr[i] = []
    for j in range(num_colors):
        arr[i] += gradients[(i + j) % num_colors]
trans = [*zip(*arr)]  # transpose


class SequentialFadePattern:
    def __init__(self, tree):
        self.tree = tree

    async def run(self):
        while True:
            for val in trans:
                self.tree.value = val
                await asyncio.sleep(0.1)
