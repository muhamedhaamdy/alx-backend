#!/usr/bin/env python3
"""Simple Flask App module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    '''get user'''
    return users.get(user_id)


@app.before_request
def before_request():
    """before_request handler"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    local = request.args.get('locale', None)
    if local and local in Config.LANGUAGES:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """renders a simple html file"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
