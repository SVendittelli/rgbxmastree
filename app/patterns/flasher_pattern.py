import asyncio

from colorzero import Color
from random import choice

from ..pixels import PixelRange

colors = [Color('red'), Color('green'), Color('blue'), Color('purple'), Color('orange'), Color('navy')]

class FlasherPattern:
    def __init__(self, tree):
        self.tree= tree

    async def run(self):
        while True:
            self.tree.value = [choice(colors) for i in PixelRange.ALL]
            await asyncio.sleep(0.5)
            self.tree.off()
            await asyncio.sleep(0.5)
