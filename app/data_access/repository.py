from ..database.models import ShortenedURL
from ..util import url_shortener


class SQLAlchemyShortenedURLRepository:
    def __init__(self, session):
        self.session = session

    def get_by_shortcode(self, shortcode):
        return (
            self.session.query(ShortenedURL)
            .filter_by(shortcode=shortcode)
            .first()
        )

    def add(self, url):
        sh_url = ShortenedURL(url)
        self.session.add(sh_url)
        self.session.flush()
        shortcode = url_shortener.shorten(sh_url.id)
        sh_url.shortcode = shortcode
        return shortcode
