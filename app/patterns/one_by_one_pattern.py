import asyncio

from colorzero import Color

colors = [Color("red"), Color("green"), Color("blue")]


class OneByOnePattern:
    """Cycle every light on the tree between red, green, and blue, one-by-one"""

    def __init__(self, tree):
        self.tree = tree

    async def run(self):
        while True:
            for color in colors:
                for pixel in self.tree:
                    pixel.color = color
                    await asyncio.sleep(0.1)
