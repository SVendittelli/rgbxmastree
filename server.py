from patterns.pattern_interface import PatternInterface
from patterns.tree import RGBXmasTree
import patterns
from flask import Flask, jsonify
app = Flask(__name__)
tree = RGBXmasTree()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/patterns', methods=['GET'])
def get_patterns():
    return jsonify(patterns.patterns)


@app.route('/patterns/<name>', methods=['POST'])
def start_pattern(name):
    if (name in patterns.patterns):
        pattern = eval('patterns.' + name + '_pattern.Pattern')
        if (issubclass(pattern, PatternInterface)):
            pattern.run(tree)
        tree.off()
    return name
