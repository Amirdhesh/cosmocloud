from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

created_id = None

def test_create():
    global created_id
    data = {
        "name": "TEST_NAME",
        "age": 20,
        "address": {"city": "TEST_CITY", "country": "TEST_COUNTRY"},
    }
    response = client.post("/api/students", json=data)
    data = response.json()
    assert response.status_code == 201
    assert "id" in data
    created_id = data["id"]
    assert created_id is not None 

def test_list():
    global created_id  
    response = client.get(f"/api/students/{created_id}")
    print(response.json())
    assert response.status_code == 200

def test_fetch():
    data = {
        "name": "TEST_NAME",
        "age": 20,
        "address": {"city": "TEST_CITY", "country": "TEST_COUNTRY"},
    }
    response = client.get(
        f"/api/students/?country={data['address']['country']}&age={data['age']}"
    )
    assert response.status_code == 200

def test_update():
    global created_id  
    response = client.patch(
        f"/api/students/{created_id}", json={"name": None, "age": 22, "address": None}
    )
    assert response.status_code == 204

def test_delete():
    global created_id  
    response = client.delete(f"/api/students/{created_id}")
    assert response.status_code == 200
