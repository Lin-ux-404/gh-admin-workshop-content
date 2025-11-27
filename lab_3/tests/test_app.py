import pytest
from app import app


@pytest.fixture()
def client():
    # Flask test client
    with app.test_client() as c:
        yield c


def test_health_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload == {"status": "ok"}


def test_sum_ok(client):
    resp = client.get("/sum?a=2&b=3")
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["result"] == 5


def test_sum_defaults_to_zero(client):
    resp = client.get("/sum")
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["result"] == 0


def test_sum_input_validation(client):
    resp = client.get("/sum?a=foo&b=1")
    assert resp.status_code == 400
    payload = resp.get_json()
    assert "error" in payload


# change to trigger actions
