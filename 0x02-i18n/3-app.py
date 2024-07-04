#!/usr/bin/env python3
"""flask babel"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """conf class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """render template"""
    return render_template('3-index.html', home_title, home_header)


if __name__ == '__main__':
    app.run()
