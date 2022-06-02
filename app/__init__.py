import os
from flask import Flask
from flask_migrate import Migrate

from .config import config
from .controllers.url_shortener import url_shortener_api

from .models.models import db

migrate = Migrate()


def create_app(config_name=os.getenv("FLASK_ENV") or "development"):
    # create and configure the app
    app = Flask(__name__)
    # Configuration
    app.config.from_object(config[config_name])
    # Database
    db.init_app(app)
    migrate.init_app(app, db)
    # Routes API
    app.register_blueprint(url_shortener_api)

    return app
