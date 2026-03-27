import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200

def test_add(client):
    r = client.get("/add/2/3")
    assert r.get_json()["result"] == 5

# def test_add_negative(client):
#     r = client.get("/add/-1/1")
#     assert r.get_json()["result"] == 0
