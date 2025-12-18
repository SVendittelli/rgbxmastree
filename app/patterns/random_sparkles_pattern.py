import asyncio
from random import random

from colorzero import Hue


def random_color():
    r = random()
    g = random()
    b = random()
    return (r, g, b)


def random_colors(n):
    return [random_color() for i in range(n)]


class RandomSparklesPattern:
    """Rapidly change each light on the tree to a random colour"""

    def __init__(self, tree):
        self.tree = tree

    async def run(self):
        while True:
            self.tree.value = random_colors(25)
            await asyncio.sleep(0.1)
