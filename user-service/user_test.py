import pytest
from app import app

@pytest.fixture
def testing_user():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_fail_register_with_empty_data(testing_user):
    response = testing_user.post("/register", json={})
    assert response.status_code == 400

def test_success_register_with_valid_data(testing_user):
    response = testing_user.post("/register", json={"username": "testing", "password": "password"})
    assert response.status_code == 201
    assert b"registered successfully" in response.data
