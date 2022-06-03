from app.util.url_shortener import (
    validate_shortcode,
    validate_url,
    shorten,
    recover_id,
)


ID_VALUE = 2260000
URL = "bdhd0"


class TestURLShortener:
    def test_validate_shortcode(self):
        valid_shortcode = "_u-as"
        invalid_shortcode_1 = ""
        invalid_shortcode_2 = " "
        invalid_shortcode_3 = "_u-as$"
        assert validate_shortcode(valid_shortcode) is True
        assert validate_shortcode(invalid_shortcode_1) is False
        assert validate_shortcode(invalid_shortcode_2) is False
        assert validate_shortcode(invalid_shortcode_3) is False

    def test_validate_url(self):
        url = "https://www.example.com"
        url_2 = "http://www.example.com"
        url_3 = "http://example.com"
        url_4 = "example.com"
        url_5 = "http://example"
        url_6 = "example"
        assert validate_url(url) is True
        assert validate_url(url_2) is True
        assert validate_url(url_3) is True
        assert validate_url(url_4) is False
        assert validate_url(url_5) is False
        assert validate_url(url_6) is False

    def test_shorten_zero(self):
        url = shorten(0)
        assert url == "a"

    def test_shorten(self):
        url = shorten(ID_VALUE)
        assert url == URL

    def test_recover_zero(self):
        id_value = recover_id("a")
        assert id_value == 0

    def test_recover_id(self):
        id_value = recover_id(URL)
        assert id_value == ID_VALUE
