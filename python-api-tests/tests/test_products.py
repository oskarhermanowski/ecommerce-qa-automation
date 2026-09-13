import pytest
import requests

pytestmark = pytest.mark.regression

def test_get_all_products(api_base_url):
    response = requests.get(f"{api_base_url}/products")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

    first_product = data["products"][0]

    assert "id" in first_product
    assert "title" in first_product
    assert "price" in first_product
    assert "stock" in first_product

    assert isinstance(first_product["id"], int)
    assert isinstance(first_product["title"], str)
    assert isinstance(first_product["price"], (int, float))
    assert isinstance(first_product["stock"], int)

    assert response.elapsed.total_seconds() < 3

def test_get_product_by_id(api_base_url):
    product_id = 1

    response = requests.get(f"{api_base_url}/products/{product_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert "title" in data
    assert "price" in data
    assert "stock" in data
    assert "category" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["price"], (int, float))

    assert response.elapsed.total_seconds() < 3

def test_get_nonexistent_product(api_base_url):
    product_id = 999999

    response = requests.get(f"{api_base_url}/products/{product_id}")

    assert response.status_code == 404
    assert response.elapsed.total_seconds() < 3

def test_create_product(api_base_url):
    payload = {
        "title": "QA Test Laptop",
        "description": "Product created by automated API test",
        "price": 2999.99,
        "stock": 10,
        "category": "laptops"
    }

    response = requests.post(
        f"{api_base_url}/products/add",
        json=payload
    )

    assert response.status_code ==201

    data = response.json()

    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["stock"] == payload["stock"]
    assert data["category"] == payload["category"]

    assert response.elapsed.total_seconds() < 3

def test_update_product(api_base_url):
    product_id = 1

    payload = {
        "title": "Updated QA Laptop",
        "price": 3499.99,
    }

    response = requests.put(
        f"{api_base_url}/products/{product_id}",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]

    assert response.elapsed.total_seconds() < 3

def test_delete_product(api_base_url):
    product_id = 1

    response = requests.delete(
        f"{api_base_url}/products/{product_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert data["isDeleted"] is True
    assert "deletedOn" in data

    assert response.elapsed.total_seconds() < 3

def test_search_products(api_base_url):
    search_query = "phone"

    response = requests.get(
        f"{api_base_url}/products/search",
        params={"q": search_query}
    )

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

    assert response.elapsed.total_seconds() < 3

@pytest.mark.parametrize("product_id", [1, 2, 3, 10, 20])
def test_get_multiple_products(api_base_url, product_id):
    response = requests.get(
        f"{api_base_url}/products/{product_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert "title" in data
    assert "price" in data

    assert response.elapsed.total_seconds() < 3