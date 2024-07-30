#!/usr/bin/env python3
"""simple flask module"with simple route"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def index():
    """render index html"""
    return render_template('3-index.html', home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == "__main__":
    app.run()
