import unittest
from app.util import url_shortener

ID_VALUE = 2260000
URL = "bdhd0"


class TestURLShortener(unittest.TestCase):
    def test_validate_url(self):
        url = "https://www.example.com"
        url_2 = "http://www.example.com"
        url_3 = "http://example.com"
        url_4 = "example.com"
        url_5 = "http://example"
        url_6 = "example"
        self.assertEqual(url_shortener.validate_url(url), True)
        self.assertEqual(url_shortener.validate_url(url_2), True)
        self.assertEqual(url_shortener.validate_url(url_3), True)
        self.assertEqual(url_shortener.validate_url(url_4), False)
        self.assertEqual(url_shortener.validate_url(url_5), False)
        self.assertEqual(url_shortener.validate_url(url_6), False)

    def test_shorten_zero(self):
        url = url_shortener.shorten(0)
        self.assertEqual(url, "a")

    def test_shorten(self):
        url = url_shortener.shorten(ID_VALUE)
        self.assertEqual(url, URL)

    def test_recover_zero(self):
        id_value = url_shortener.recover_id("a")
        self.assertEqual(id_value, 0)

    def test_recover_id(self):
        id_value = url_shortener.recover_id(URL)
        self.assertEqual(id_value, ID_VALUE)
