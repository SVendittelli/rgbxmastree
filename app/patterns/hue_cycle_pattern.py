import asyncio

from colorzero import Color, Hue

class HueCyclePattern:
    def __init__(self, tree):
        self.tree= tree

    async def run(self):
        self.tree.color = Color('red')

        while True:
            self.tree.color += Hue(deg=1)
            await asyncio.sleep(0.1)
