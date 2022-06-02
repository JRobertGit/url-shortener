import os
from flask import Flask

from .config import config
from .controllers.url_shortener import url_shortener_api


def create_app(config_name=os.getenv("FLASK_ENV") or "development"):
    # create and configure the app
    app = Flask(__name__)
    # Configuration
    app.config.from_object(config[config_name])
    # Routes API
    app.register_blueprint(url_shortener_api)

    return app
