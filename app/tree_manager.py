import asyncio

from .patterns import (
    FadePattern,
    FlasherPattern,
    HueCyclePattern,
    LayerPattern,
    OneByOnePattern,
    RandomFadePattern,
    RandomSparklesPattern,
    RGBPattern,
    SequentialFadePattern,
    TwinklePattern,
    WhooshPattern,
    patterns,
)
from .tree import RGBXmasTree


class TreeManager:
    def __init__(self):
        self.tree = RGBXmasTree()
        self.active_task = None
        self.patterns = patterns

    async def run_pattern(self, pattern_name: str):
        await self.off()

        pattern = self.patterns.get(pattern_name)
        if not pattern:
            raise ValueError("Pattern not found")

        # Inject the tree instance into the pattern constructor
        instance = pattern(self.tree)

        # Start the pattern's run method as a task
        self.active_task = asyncio.create_task(instance.run())

    async def off(self):
        if self.active_task:
            self.active_task.cancel()
            try:
                await self.active_task
            except asyncio.CancelledError:
                pass
            self.active_task = None
            self.tree.off()
