# -*- coding: utf-8 -*-

import os
from flask import Flask


def create_app():
    # creates and configures the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'country_app.sqlite'),
    )
    # loades the instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)
    # ensures the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import country_city
    app.register_blueprint(country_city.bp)
    app.add_url_rule('/<int:id>', endpoint='index')

    return app
