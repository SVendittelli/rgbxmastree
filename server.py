import os

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/patterns', methods=['GET'])
def patterns():
    patterns = []
    for file in os.listdir('/home/pi/projects/rgbxmastree/patterns'):
        patterns.append(file[:-3])
    patterns.sort()
    return jsonify(patterns)
