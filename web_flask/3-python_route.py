#!/usr/bin/python3
"""Script that starts a flask web app.
"""
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Route / definition

    Returns:
        [string]: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route /hbnb definition

    Returns:
        [string]: "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Route /c/<text> definition
    receives a varible text

    Returns:
        [string]: "C <text>"
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def pyisfun(text):
    """Route /python/(<text>) definition
    receives a varible text

    Returns:
        [string]: "Python <text>"
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
