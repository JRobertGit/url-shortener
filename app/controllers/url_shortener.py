from flask import abort, Blueprint, jsonify, request
import random

from ..util import url_shortener


url_shortener_api = Blueprint("url_shortener_api", __name__)
"""URL Shortener API"""


@url_shortener_api.route("/", methods=["GET"])
def test():
    return jsonify("URL Shortner is Up and Running!")


@url_shortener_api.route("/<route>", methods=["GET"])
def redirect_to_url(route):
    return jsonify(route)


@url_shortener_api.route("/api/shortener/<shortcode>", methods=["GET"])
def get_shortened_url(shortcode):
    return jsonify(shortcode)


@url_shortener_api.route("/api/shortener", methods=["POST"])
def shorten_url():
    data = request.get_json()
    if not ("url" in data):
        return abort(400, "No URL provided")
    if not url_shortener.validate_url(data["url"]):
        return abort(400, "Invalid URL provided")
    # TODO: Add Data Access Layer
    id = random.randint(3000000, 10000000)
    shortened_url = url_shortener.shorten(id)
    return jsonify(shortened_url)
