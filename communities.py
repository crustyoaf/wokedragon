from sqlalchemy import or_

from extensions import db
from models import Community

COMMUNITIES = [
    {
        "name": "Lorem ipsum",
        "slug": "lorem-ipsum",
        "description": "Lorem ipsum dolor sit amet.",
        "members": 124
    },
    {
        "name": "Dolor sit amet",
        "slug": "dolor-sit-amet",
        "description": "Consectetur adipiscing elit.",
        "members": 86
    },
    {
        "name": "Consectetur adipiscing",
        "slug": "consectetur-adipiscing",
        "description": "Sed do eiusmod tempor incididunt.",
        "members": 52
    },
    {
        "name": "Mindful Living",
        "slug": "mindful-living",
        "description": "A space for reflection and everyday wellbeing.",
        "members": 31
    }
]

def get_community_by_slug(slug):
    return db.session.scalar(
        db.select(Community).where(Community.slug == slug)
    )


def search_communities(query):
    query = query.strip()
    statement = db.select(Community).order_by(Community.name)

    if query:
        statement = statement.where(
            or_(
                Community.name.icontains(query, autoescape=True),
                Community.description.icontains(query, autoescape=True),
            )
        )

    return db.session.scalars(statement).all()