from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree
from colorzero import Color

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

class Pattern(PatternInterface):
    def run(tree):
        pass

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            for color in colors:
                tree.color = color
    except (KeyboardInterrupt, SystemExit):
        tree.off()
