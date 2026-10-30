from flask import Flask, render_template, request, abort

from communities import COMMUNITIES, get_community_by_slug

app = Flask(__name__)
app.config["TESTING"] = False


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
        communities=[
    community for community in COMMUNITIES
    if search_query.lower() in (
        community["name"] + " " + community["description"]
    ).lower()
]
    )
    
@app.route("/community/<slug>")
def community_detail(slug):
    community = get_community_by_slug(slug)

    community = next(
    (item for item in COMMUNITIES if item["slug"] == slug),
    None
)

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
    
if __name__ == "__main__":
    app.run(debug=True)