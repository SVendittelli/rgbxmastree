import asyncio
from math import ceil, floor
from random import choice, randrange, uniform

from colorzero import Color

from ..pixels import PixelRange

green = Color("green")
red = Color("red")


class WhooshPattern:
    """Light the tree up green, layer-by-layer, until it randomly flashes red"""

    def __init__(self, tree):
        self.tree = tree

    async def run(self):
        while True:
            limit = randrange(
                500, 580
            )  # expected 540 = seconds in 18 minutes / average cycle time for green (2 seconds)
            print("Limit: {}".format(limit))

            count = 0
            while count < limit:
                seconds = ceil((limit - count) * 1.5)
                minutes = floor(seconds / 60)
                print(
                    "{:3} / {:3} ({:02}:{:02} approx.)".format(
                        count + 1, limit, minutes, seconds % 60
                    )
                )
                await asyncio.sleep(uniform(0.1, 2))  # expected 1.1
                self.tree.set_range(PixelRange.BOTTOM, green)
                await asyncio.sleep(0.1)
                self.tree.set_range(PixelRange.MIDDLE, green)
                await asyncio.sleep(0.1)
                self.tree.set_range(PixelRange.TOP, green)
                await asyncio.sleep(0.1)
                self.tree.set_range(PixelRange.STAR, Color("gold"))
                await asyncio.sleep(0.5)
                self.tree.off()
                count = count + 1

            # flash red 7 times
            for i in range(7):
                await asyncio.sleep(0.25)
                self.tree.set_range(PixelRange.STAR, red)
                await asyncio.sleep(0.25)
                self.tree.off()
