
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
    return next(
        (item for item in COMMUNITIES if item["slug"] == slug),
        None
    )
    
def search_communities(query):
    query = query.strip().lower()

    if not query:
        return COMMUNITIES

    return [
        community for community in COMMUNITIES
        if query in community["name"].lower()
        or query in community["description"].lower()
    ]