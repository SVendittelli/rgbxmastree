from patterns.pattern_interface import PatternInterface
from .tree import RGBXmasTree
from colorzero import Color

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

class Pattern(PatternInterface):
    def apply(self, tree, thread):
        for color in colors:
            if (thread.stopped()):
                break
            tree.color = color

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            for color in colors:
                tree.color = color
    except (KeyboardInterrupt, SystemExit):
        tree.off()
