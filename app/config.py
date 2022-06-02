import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_DB = "sqlite:///" + os.path.join(
    BASE_DIR, "database/shortened_urls.db"
)
ENV_DB = os.getenv("DATABASE_URL") or DEFAULT_DB


class Config:
    DEBUG = False


class DEV(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DEFAULT_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class PROD(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ENV_DB


config = dict(development=DEV, production=PROD)
