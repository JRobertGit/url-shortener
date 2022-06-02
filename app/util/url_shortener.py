import re


# URL Shortener
# Allowed Symbols, "Alphabet"
# Base Length 38
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789_-"
BASE = len(ALPHABET)

# Django URL Validation Regex
URL_REGEX = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # noqa
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def validate_url(url):
    return re.match(URL_REGEX, url) is not None


def validate_shortcode(shortcode):
    if len(shortcode) == 0:
        return False
    for c in shortcode:
        if not (c in ALPHABET):
            return False
    return True


def shorten(id_value):
    if id_value == 0:
        return ALPHABET[0]

    url = ""
    while id_value > 0:
        url = ALPHABET[id_value % BASE] + url
        id_value //= BASE

    return url


def recover_id(url):
    id = 0
    for c in url:
        id = (id * BASE) + ALPHABET.index(c)
    return id
