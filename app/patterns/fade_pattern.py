import asyncio

from colorzero import Color

from ..pixels import PixelRange

colors = [Color('red'), Color('green'), Color('blue')]
num_colors = len(colors)

class FadePattern:
    def __init__(self, tree):
        self.tree= tree

    async def run(self):
        self.tree.set_range(PixelRange.STAR, Color('gold'))

        while True:
            for i in range(num_colors):
                for col in colors[i].gradient(colors[(i+1) % num_colors], steps=100):
                    self.tree.set_range(PixelRange.NOT_STAR, col)
                    await asyncio.sleep(0.1)
