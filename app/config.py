import os

basedir = os.path.abspath(os.path.dirname(__file__))

env_db = os.getenv("DATABASE_URL")


class Config:
    DEBUG = False


class DEV(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "database/shortened_urls.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TEST(Config):
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "database/shortened_urls.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


class PROD(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = env_db


config = dict(dev=DEV, test=TEST, prod=PROD)
