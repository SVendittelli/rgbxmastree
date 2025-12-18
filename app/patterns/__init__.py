from enum import Enum

from pydantic import BaseModel

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


class PatternName(str, Enum):
    fade = "fade"
    flasher = "flasher"
    hue_cycle = "hue_cycle"
    layer = "layer"
    one_by_one = "one_by_one"
    random_fade = "random_fade"
    random_sparkles = "random_sparkles"
    rgb = "rgb"
    sequential_fade = "sequential_fade"
    twinkle = "twinkle"
    whoosh = "whoosh"


class Pattern(BaseModel):
    name: PatternName
    description: str


patterns = {
    PatternName.fade: FadePattern,
    PatternName.flasher: FlasherPattern,
    PatternName.hue_cycle: HueCyclePattern,
    PatternName.layer: LayerPattern,
    PatternName.one_by_one: OneByOnePattern,
    PatternName.random_fade: RandomFadePattern,
    PatternName.random_sparkles: RandomSparklesPattern,
    PatternName.rgb: RGBPattern,
    PatternName.sequential_fade: SequentialFadePattern,
    PatternName.twinkle: TwinklePattern,
    PatternName.whoosh: WhooshPattern,
}
pattern_names = [
    {"name": name, "description": pattern.__doc__} for name, pattern in patterns.items()
]
