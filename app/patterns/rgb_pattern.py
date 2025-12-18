import asyncio

from colorzero import Color

colors = [Color("red"), Color("green"), Color("blue")]


class RGBPattern:
    """Make the whole tree red, green, then blue in sequence"""

    def __init__(self, tree):
        self.tree = tree

    async def run(self):
        while True:
            for color in colors:
                self.tree.color = color
                await asyncio.sleep(1)
