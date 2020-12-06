from stoppable_thread import StoppableThread
from patterns.pattern_interface import PatternInterface
from patterns.tree import RGBXmasTree
import atexit
import patterns
from flask import Flask, jsonify

app = Flask(__name__)
tree = RGBXmasTree()
tree_thread = StoppableThread()

def interupt():
    global tree
    global tree_thread
    if tree_thread.is_alive():
        tree_thread.stop()
        tree_thread.join()
    tree.off()

atexit.register(interupt)

def apply_pattern(pattern):
    global tree
    global tree_thread
    while not tree_thread.stopped():
        pattern.apply(tree, tree_thread)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/patterns', methods=['GET'])
def get_patterns():
    return jsonify(patterns.patterns)

@app.route('/patterns/<name>', methods=['POST'])
def start_pattern(name):
    if (name in patterns.patterns):
        pattern = eval('patterns.' + name + '_pattern.Pattern()')
        if (issubclass(pattern.__class__, PatternInterface)):
            global tree_thread
            interupt()
            tree_thread = StoppableThread(target=apply_pattern, args=(pattern,))
            tree_thread.start()

    return name
