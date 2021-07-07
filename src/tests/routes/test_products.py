import json


def test_create_product(client):
    data = {"title": "Pizza", "description": "tomato avocado and bacon"}
    response = client.post("/products/create", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Pizza"
    assert response.json()["description"] == "tomato avocado and bacon"


def test_get_job(client):
    data = {"title": "Pizza", "description": "tomato avocado and bacon"}

    client.post("/products/create", json.dumps(data))

    response = client.get("products/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Pizza"
