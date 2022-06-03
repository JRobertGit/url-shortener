import json


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"URL Shortner is Up and Running!" in response.data


def test_redirect_to_url(client):
    # Valid Shortcode
    response = client.get("/b")
    assert response.status_code == 302
    assert b"https://www.google.com" in response.data

    # Non-existent Shortcode
    response = client.get("/c")
    assert response.status_code == 404

    # Invalid Shortcode
    response = client.get("/sdf$")
    assert response.status_code == 404


def test_get_shortened_url(client):
    # Valid Shortcode
    response = client.get("/api/shortener/b")
    assert response.status_code == 200
    assert b"https://www.google.com" in response.data

    # Non-existent Shortcode
    response = client.get("/api/shortener/c")
    assert response.status_code == 404

    # Invalid Shortcode
    response = client.get("/api/shortener/sdf$")
    assert response.status_code == 404


def test(client):
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {"url": "https://www.youtube.com"}
    url = "/api/shortener"

    # Valid URL
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    response.status_code == 200
    assert b"c" in response.data

    # Missing URL
    response = client.post(url, headers=headers)
    response.status_code == 400
    assert (
        b"<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>Bad Request</h1>\n<p>Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)</p>\n"  # noqa
        in response.data
    )

    # Missing URL
    data = {"ur": "https://www.youtube.com"}
    response = client.post(url, data=json.dumps(data), headers=headers)
    response.status_code == 400
    assert (
        b"<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>Bad Request</h1>\n<p>No URL provided</p>\n"  # noqa
        in response.data
    )

    # Invalid URL
    data = {"url": "www.youtube"}
    response = client.post(url, data=json.dumps(data), headers=headers)
    response.status_code == 400
    assert (
        b"<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>Bad Request</h1>\n<p>Invalid URL provided</p>\n"  # noqa
        in response.data
    )
