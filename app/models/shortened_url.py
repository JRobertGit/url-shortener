from sqlalchemy.schema import Sequence

from .. import db


class ShortenedURL(db.Model):
    """Shortened URL Model"""

    __tablename__ = "shortened_url"

    id = db.Column(
        db.Integer,
        Sequence("id_sequence", start=1000000, increment=1),
        primary_key=True,
    )
    url = db.Column(db.String)
    shortcode = db.Column(db.String)
    clicks = db.Column(db.Integer)
    creation_date = db.Column(db.DateTime)
    last_visit = db.Column(db.DateTime)
