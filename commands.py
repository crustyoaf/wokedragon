import click
from flask.cli import with_appcontext

from extensions import db
from models import Community

SEED_COMMUNITIES = [
    {
        "name": "Lorem ipsum",
        "slug": "lorem-ipsum",
        "description": "Lorem ipsum dolor sit amet.",
    },
    {
        "name": "Dolor sit amet",
        "slug": "dolor-sit-amet",
        "description": "Consectetur adipiscing elit.",
    },
    {
        "name": "Consectetur adipiscing",
        "slug": "consectetur-adipiscing",
        "description": "Sed do eiusmod tempor incididunt.",
    },
    {
        "name": "Mindful Living",
        "slug": "mindful-living",
        "description": "A space for reflection and everyday wellbeing.",
    },
]


@click.command("seed")
@with_appcontext
def seed():
    """Add placeholder communities for local development."""
    for item in SEED_COMMUNITIES:
        existing = db.session.scalar(
            db.select(Community).where(Community.slug == item["slug"])
        )
        if existing is None:
            db.session.add(Community(**item))

    db.session.commit()
    print("Seeded communities.")