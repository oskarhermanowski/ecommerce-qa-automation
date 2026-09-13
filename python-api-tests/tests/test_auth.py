import pytest
import requests

@pytest.mark.smoke
def test_login_successful(api_base_url):
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(
        f"{api_base_url}/auth/login",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "accessToken" in data
    assert "refreshToken" in data
    assert data["username"] == "emilys"
    assert isinstance(data["id"], int)
    assert response.elapsed.total_seconds() < 3

def test_login_invalid_credentials(api_base_url):
    payload = {
        "username": "emilys",
        "password": "wrongpassword"
    }

    response = requests.post(
        f"{api_base_url}/auth/login",
        json=payload
    )

    assert response.status_code == 400

    data = response.json()

    assert "message" in data
    assert data["message"] == "Invalid credentials"
    assert "accessToken" not in data
    assert response.elapsed.total_seconds() < 3

def test_login_missing_password(api_base_url):
    payload = {
        "username": "emilys"
    }

    response = requests.post(
        f"{api_base_url}/auth/login",
        json=payload
    )

    assert response.status_code == 400

    data = response.json()

    assert "message" in data
    assert data["message"] == "Username and password required"
    assert "accessToken" not in data
    assert "refreshToken" not in data
    assert response.elapsed.total_seconds() < 3

@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ("emilys", "wrongpassword", 400),
        ("wronguser", "emilyspass", 400),
        ("", "", 400),
    ]
)
def test_login_various_invalid_data(api_base_url, username, password, expected_status):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(
        f"{api_base_url}/auth/login",
        json=payload
    )

    assert response.status_code == expected_status
    assert response.elapsed.total_seconds() < 3