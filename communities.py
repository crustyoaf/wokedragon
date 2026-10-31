from sqlalchemy import or_

from extensions import db
from models import Community


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