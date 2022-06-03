import pytest

from app import create_app, db
from app.database.models import ShortenedURL
from app.util.url_shortener import shorten


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.testing = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    client = app.test_client()
    with app.app_context():
        db.create_all()
        sh_url1 = ShortenedURL("https://www.google.com")
        db.session.add(sh_url1)
        db.session.flush()
        sh_url1.shortcode = shorten(sh_url1.id)
        db.session.commit()
    yield client
