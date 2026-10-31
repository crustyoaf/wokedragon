import pytest
from app import create_app
from communities import get_community_by_slug, search_communities


@pytest.fixture
def app():
    app = create_app()
    app.config.update(TESTING=True)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def app_context(app):
    with app.app_context():
        yield

def test_existing_community(app_context):
    community = get_community_by_slug("lorem-ipsum")

    assert community is not None
    assert community.name == "Lorem ipsum"


def test_missing_community(app_context):
    community = get_community_by_slug("poop")

    assert community is None


def test_community_page_returns_200(client):
    response = client.get("/community/lorem-ipsum")

    assert response.status_code == 200
    assert b"Lorem ipsum" in response.data


def test_missing_community_page_returns_404(client):   
    response = client.get("/community/poop")

    assert response.status_code == 404

    
def test_explore_page_shows_communities(client):
    

    response = client.get("/explore")

    assert response.status_code == 200
    assert b"Lorem ipsum" in response.data
    assert b"Dolor sit amet" in response.data
    assert b"Consectetur adipiscing" in response.data
    
def test_home_page_returns_200(client):   
    response = client.get("/")

    assert response.status_code == 200
    assert b"Home" in response.data

def test_explore_page_has_navigation(client):
    response = client.get("/explore")

    assert b'href="/"' in response.data
    assert b'href="/explore"' in response.data
    
def test_home_page_returns_html(client):
    response = client.get("/")

    assert response.content_type == "text/html; charset=utf-8"
    
def test_search_is_case_insensitive(app_context):
    results = search_communities("MINDFUL")

    assert [c.slug for c in results] == ["mindful-living"]


def test_empty_search_returns_all_communities(app_context):
    assert len(search_communities("   ")) == 4
    
    
def test_explore_search_with_no_results(client):
    response = client.get("/explore?q=xyz")

    assert response.status_code == 200
    assert b"No communities match" in response.data
    assert b"Lorem ipsum" not in response.data