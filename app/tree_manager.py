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
)
from .tree import RGBXmasTree


class TreeManager:
    def __init__(self):
        self.tree = RGBXmasTree()
        self.active_task = None
        # Map strings to classes for easy lookup
        self.patterns = {
            "fade": FadePattern,
            "flasher": FlasherPattern,
            "hue_cycle": HueCyclePattern,
            "layer": LayerPattern,
            "one_by_one": OneByOnePattern,
            "random_fade": RandomFadePattern,
            "random_sparkles": RandomSparklesPattern,
            "rgb": RGBPattern,
            "sequential_fade": SequentialFadePattern,
            "twinkle": TwinklePattern,
            "whoosh": WhooshPattern,
        }

    async def run_pattern(self, pattern_name: str):
        await self.stop_current()

        pattern_class = self.patterns.get(pattern_name)
        if not pattern_class:
            raise ValueError("Pattern not found")

        # Inject the tree instance into the pattern constructor
        instance = pattern_class(self.tree)

        # Start the pattern's run method as a task
        self.active_task = asyncio.create_task(instance.run())

    async def stop_current(self):
        if self.active_task:
            self.active_task.cancel()
            try:
                await self.active_task
            except asyncio.CancelledError:
                pass
            self.active_task = None
            self.tree.off()
