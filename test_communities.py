import pytest
from app import app
from communities import get_community_by_slug


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

    app.config["TESTING"] = False

def test_existing_community():
    community = get_community_by_slug("lorem-ipsum")

    assert community is not None
    assert community["name"] == "Lorem ipsum"


def test_missing_community():
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
    
    