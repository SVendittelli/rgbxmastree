from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

if __name__ == '__main__':
    tree = RGBXmasTree()
    try:
        while True:
            for color in colors:
                tree.color = color
    except (KeyboardInterrupt, SystemExit):
        tree.off()
