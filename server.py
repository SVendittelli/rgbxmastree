from threading import current_thread
from flask.helpers import make_response
from stoppable_thread import StoppableThread
from patterns.pattern_interface import PatternInterface
from patterns.tree import RGBXmasTree
import atexit
import patterns
from flask import Flask, jsonify, request

app = Flask(__name__)
tree = RGBXmasTree()
tree_thread = StoppableThread()
current_pattern = ''

def interupt():
    if tree_thread.is_alive():
        app.logger.info('Stopping (%s)', current_pattern)
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

@app.route('/patterns', methods=['GET', 'POST'])
def get_patterns():
    if request.method == 'GET':
        return jsonify(patterns.patterns)
    
    if request.is_json:
        global current_pattern
        current_pattern = str(request.get_json()['name'])
        start()
        return jsonify_no_content()
    else:
        # The request body wasn't JSON so return a 400 HTTP status code
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@app.route('/status', methods=['GET', 'POST'])
def status():
    if request.method == 'GET':
        return jsonify({
            'running': tree_thread.is_alive(),
            'pattern': current_pattern
        })

    if request.is_json:
        status = request.get_json()['status']
        if (status == 'stop'):
            interupt()
        elif (status == 'start'):
            start()
        return jsonify_no_content()
    else:
        # The request body wasn't JSON so return a 400 HTTP status code
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

def start():
    global current_pattern
    if (current_pattern in patterns.patterns):
        pattern = eval('patterns.' + current_pattern + '_pattern.Pattern()')
        if (issubclass(pattern.__class__, PatternInterface)):
            global tree_thread
            interupt()
            tree_thread = StoppableThread(target=apply_pattern, args=(pattern,))
            app.logger.info('starting pattern (%s)', current_pattern)
            tree_thread.start()

def jsonify_no_content():
    response = make_response('', 204)
    response.mimetype = app.config['JSONIFY_MIMETYPE']
 
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
