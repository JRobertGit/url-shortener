import unittest
from app.util import url_shortener

ID_VALUE = 2260000
URL = "bdhd0"


class TestURLShortener(unittest.TestCase):
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
