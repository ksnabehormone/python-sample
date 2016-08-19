import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    users = {1: {'id': 1, 'name': 'foo'},2: {'id': 2, 'name': 'bar'}}
    return jsonify(users)

if __name__ == '__main__':
    app.run()
