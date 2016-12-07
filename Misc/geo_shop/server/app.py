# -*- coding: utf-8 -*-

import os
from flask import Flask
from server.api import api, data_path

from server.csv_data_handler import CSVStaticData

def create_app(settings_overrides=None):
    app = Flask(__name__)
    app.secret_key = 'secret'
    configure_settings(app, settings_overrides)
    configure_blueprints(app)
    with app.app_context():

        app.csv_static_data = CSVStaticData(data_path)
    return app


def configure_settings(app, settings_override):
    parent = os.path.dirname(__file__)
    data_path = os.path.join(parent, '..', 'data')
    app.config.update({
        'DEBUG': True,
        'TESTING': False,
        'DATA_PATH': data_path,
        'CSRF_ENABLED': False,
        'WTF_CSRF_ENABLED': False,
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    app.register_blueprint(api)
