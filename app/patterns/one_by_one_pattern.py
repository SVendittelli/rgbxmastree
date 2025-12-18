import asyncio

from colorzero import Color

colors = [Color('red'), Color('green'), Color('blue')]

class OneByOnePattern:
    def __init__(self, tree):
        self.tree= tree

    async def run(self):
        while True:
            for color in colors:
                for pixel in self.tree:
                    pixel.color = color
                    await asyncio.sleep(0.1)
