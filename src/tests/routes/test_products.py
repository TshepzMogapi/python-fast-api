import json


def test_create_product(client):
    data = {"title": "Pizza", "description": "tomato avocado and bacon"}
    response = client.post("/products/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Pizza"
    assert response.json()["description"] == "tomato avocado and bacon"


def test_get_produt(client):
    data = {"title": "Pizza", "description": "tomato avocado and bacon"}
    client.post("/products/", json.dumps(data))
    response = client.get("products/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Pizza"


def test_get_all_products(client):
    data = {"title": "Pizza", "description": "Italian avocado pizaa"}
    data_2 = {"title": "Pizza 2", "description": "Italian avocado pizaa"}
    client.post("/products/", json.dumps(data))
    client.post("/products/", json.dumps(data_2))
    response = client.get("products/")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "Pizza"
    assert response.json()[1]["title"] == "Pizza 2"


def test_update_products_(client):
    data = {"title": "Pizza", "description": "tomato avocado and bacon"}
    client.post("/products/", json.dumps(data))
    data["title"] = "New Italian Pizza"
    response = client.put("products/1", json.dumps(data))
    assert response.json()["message"] == "updated"
