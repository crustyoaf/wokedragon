import os

from flask import Flask

from communities import COMMUNITIES
from extensions import db, migrate
from models import Community
from routes import bp

app = Flask(__name__)
app.config["TESTING"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db.init_app(app)
migrate.init_app(app, db)
app.register_blueprint(bp)



    
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