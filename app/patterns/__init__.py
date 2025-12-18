from .fade_pattern import FadePattern
from .flasher_pattern import FlasherPattern
from .hue_cycle_pattern import HueCyclePattern
from .layer_pattern import LayerPattern
from .one_by_one_pattern import OneByOnePattern
from .random_fade_pattern import RandomFadePattern
from .random_sparkles_pattern import RandomSparklesPattern
from .rgb_pattern import RGBPattern
from .sequential_fade_pattern import SequentialFadePattern
from .twinkle_pattern import TwinklePattern
from .woosh_pattern import WhooshPattern

patterns = {
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
pattern_names = [
    {"name": name, "description": pattern.__doc__} for name, pattern in patterns.items()
]
