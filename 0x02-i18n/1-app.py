#!/usr/bin/env python3
'''flask babel'''
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    '''balbel config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
appbabel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def welcome():
    '''render template'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
