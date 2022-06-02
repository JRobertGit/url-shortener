# URL Shortener
# Allowed Symbols, "Alphabet"
# Base Length 38
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789_-"
BASE = len(ALPHABET)


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
