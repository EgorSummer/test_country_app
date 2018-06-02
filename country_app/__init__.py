# -*- coding: utf-8 -*-

import os
from flask import Flask


def create_app():
    # creates and configures the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SEKRET_KEY='dev'
    )
    # loades the instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)
    # ensures the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
