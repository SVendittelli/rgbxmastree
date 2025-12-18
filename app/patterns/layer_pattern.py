import asyncio

from colorzero import Color

from ..pixels import PixelRange

class LayerPattern:
    def __init__(self, tree):
        self.tree= tree

    async def run(self):
        while True:
            self.tree.set_range(PixelRange.STAR, Color('gold'))
            await asyncio.sleep(0.2)
            self.tree.set_range(PixelRange.TOP, Color('red'))
            await asyncio.sleep(0.2)
            self.tree.set_range(PixelRange.MIDDLE, Color('green'))
            await asyncio.sleep(0.2)
            self.tree.set_range(PixelRange.BOTTOM, Color('blue'))
            await asyncio.sleep(0.5)
            self.tree.off()
            await asyncio.sleep(0.5)
