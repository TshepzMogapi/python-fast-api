import json


def test_create_user(client):
  data = {"email":"test@test.com", "password": "testing"}
  response = client.post("/users/", json.dumps(data))
  assert response.status_code == 200
  assert response.json()["email"] == "test@test.com"
  assert response.json()["is_active"] == True