from util import url_shortener


def main():
    id_value = 2260000
    url = url_shortener.shorten(id_value)
    print(url)
    print(url_shortener.recover_id(url))


if __name__ == "__main__":
    main()
