from flask import Blueprint


url_shortener_api = Blueprint("url_shortener_api", __name__)
"""URL Shortener API"""


@url_shortener_api.route("/", methods=["GET"])
def get_shortened_url():
    return "Hello World!"
