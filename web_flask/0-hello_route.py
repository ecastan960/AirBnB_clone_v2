#!/usr/bin/python3
"""Script that starts a flask web app.
"""
from flask import Flask, redirect, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """Route / definition

    Returns:
        [string]: "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
