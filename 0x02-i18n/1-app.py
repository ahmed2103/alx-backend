#!/usr/bin/env python3
"""simple flask module"with simple route"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)



@app.route("/")
def index():
    """render index html"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
