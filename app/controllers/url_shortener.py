from flask import abort, Blueprint, jsonify, redirect, request


from ..data_access.unit_of_work import SQLAlchemyUnitOfWork
from ..database.models import db
from ..util import url_shortener

uow = SQLAlchemyUnitOfWork(db.session)


url_shortener_api = Blueprint("url_shortener_api", __name__)
"""URL Shortener API"""


@url_shortener_api.route("/", methods=["GET"])
def test():
    return jsonify("URL Shortner is Up and Running!")


@url_shortener_api.route("/<route>", methods=["GET"])
def redirect_to_url(route):
    sh_url = uow.shorteded_urls.get_by_shortcode(route)

    if not sh_url:
        return abort(404)

    return redirect(sh_url.url, 302)


@url_shortener_api.route("/api/shortener/<shortcode>", methods=["GET"])
def get_shortened_url(shortcode):
    sh_url = uow.shorteded_urls.get_by_shortcode(shortcode)

    if not sh_url:
        return abort(404)

    return jsonify(sh_url.url)


@url_shortener_api.route("/api/shortener", methods=["POST"])
def shorten_url():
    data = request.get_json()

    if not ("url" in data):
        return abort(400, "No URL provided")

    if not url_shortener.validate_url(data["url"]):
        return abort(400, "Invalid URL provided")

    shortcode = uow.shorteded_urls.add(data["url"])
    uow.commit()

    return jsonify(shortcode)
