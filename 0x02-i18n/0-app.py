#!/usr/bin/env python3
"""simple flask module"with simple route"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """render index html"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
