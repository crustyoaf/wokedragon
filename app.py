import os
from models import Community

from extensions import db, migrate

from flask import Flask, render_template, request, abort

from communities import COMMUNITIES, get_community_by_slug, search_communities

app = Flask(__name__)
app.config["TESTING"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db.init_app(app)
migrate.init_app(app, db)


# Show the home page when someone visits the root URL.
@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home"
    )	

@app.route("/explore")
def explore():
    search_query = request.args.get("q", "").strip()

    return render_template(
        "explore.html",
        page_title="Explore",
        search_query=search_query,
        communities=search_communities(search_query)
    )
    
@app.route("/community/<slug>")
def community_detail(slug):
    community = get_community_by_slug(slug)


    if community is None:
        abort(404)

    return render_template(
        "community.html",
        page_title=community["name"],
        community=community
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
    
@app.cli.command("seed")
def seed():
    """Add placeholder communities for local development."""
    for item in COMMUNITIES:
        existing = db.session.scalar(
            db.select(Community).where(Community.slug == item["slug"])
        )
        if existing is None:
            db.session.add(
                Community(
                    name=item["name"],
                    slug=item["slug"],
                    description=item["description"],
                )
            )

    db.session.commit()
    print("Seeded communities.")    
       
    
if __name__ == "__main__":
    app.run(debug=True)