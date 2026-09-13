import pytest
import requests

@pytest.mark.smoke
def test_api_health_check(api_base_url):
    response = requests.get(f"{api_base_url}/test")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["method"] == "GET"
    assert response.elapsed.total_seconds() < 3