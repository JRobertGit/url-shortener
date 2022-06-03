from app.database.models import ShortenedURL


def test_shortened_url():
    sh_url = ShortenedURL("http://www.example.com")
    assert sh_url.url == "http://www.example.com"
    assert sh_url.shortcode is None
