from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ShortenedURL(db.Model):
    """Shortened URL Model"""

    __tablename__ = "shortened_url"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    shortcode = db.Column(db.String, index=True, unique=True)

    def __init__(self, url):
        self.url = url
