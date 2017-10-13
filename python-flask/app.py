from flask import Flask, jsonify
from utils import fibonacci
from data import models

app = Flask(__name__)


@app.route('/hello_world', methods=['GET'])
def hello():
    return jsonify({'hello': 'World'})


@app.route('/hello/<user>', methods=['GET'])
def hello_user(user: str):
    return jsonify({'hello': '{}'.format(user)})


@app.route('/fib30', methods=['GET'])
def fib30():
    return jsonify({'fibonacci30': fibonacci.fibonacci(30)})


if __name__ == '__main__':
    app.run()
