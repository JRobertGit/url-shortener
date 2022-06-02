from .repository import SQLAlchemyShortenedURLRepository


class SQLAlchemyUnitOfWork:
    def __init__(self, session):
        self.session = session
        self.shorteded_urls = SQLAlchemyShortenedURLRepository(self.session)

    def commit(self):
        self.session.commit()
