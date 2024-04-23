import logging.config
import os

from flask import Flask
import click

from bhs_cadences import views, commands
from bhs_cadences.logging import init_logging


def create_app(config_overrides=None):
    init_logging()  # should be configured before any access to app.logger

    app = Flask(__name__)
    app.config.from_object("bhs_cadences.defaults")
    app.config.from_prefixed_env()

    if config_overrides is not None:
        app.config.from_mapping(config_overrides)

    app.register_blueprint(views.bp)
    app.register_blueprint(commands.bp)

    app.config['DATA_DIR'] = 'data'

    # for var in ['DATA_DIR']:
    #     app.config[var] = os.environ.get(var)

    return app

