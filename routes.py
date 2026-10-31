from flask import Blueprint, abort, render_template, request

from communities import get_community_by_slug, search_communities

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("home.html", page_title="Home")


@bp.route("/explore")
def explore():
    search_query = request.args.get("q", "").strip()

    return render_template(
        "explore.html",
        page_title="Explore",
        search_query=search_query,
        communities=search_communities(search_query),
    )


@bp.route("/community/<slug>")
def community_detail(slug):
    community = get_community_by_slug(slug)

    if community is None:
        abort(404)

    return render_template(
        "community.html",
        page_title=community.name,
        community=community,
    )


@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404