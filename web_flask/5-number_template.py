#!/usr/bin/python3
"""
A Flask web application with routes and rendering HTML templates.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # Replace underscores (_) with spaces in the text variable
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    # Replace underscores (_) with spaces in the text variable
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number_template.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
