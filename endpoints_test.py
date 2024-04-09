from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class Test:
    def __init__(self):
        self.id = None
        self.data = {
            "name": "TEST_NAME",
            "age": 20,
            "address": {"city": "TEST_CITY", "country": "TEST_COUNTRY"},
        }

    def create_test(self):
        response = client.post("/api/students", json=self.data)
        data = response.json()
        assert response.status_code == 201
        assert "id" in data
        self.id = data["id"]

    def list_test(self):
        response = client.get(f"/api/students/{self.id}")
        assert response.status_code == 200

    def fetch_test(self):
        response = client.get(
            f"/api/students/?country={self.data['address']['country']}&age={self.data['age']}"
        )
        assert response.status_code == 200

    def update_test(self):
        response = client.patch(
            f"/api/students/{self.id}", json={"name": None, "age": 22, "address": None}
        )
        assert response.status_code == 204

    def delete_test(self):
        response = client.delete(f"/api/students/{self.id}")
        assert response.status_code == 200


test_instance = Test()


test_instance.create_test()
test_instance.list_test()
test_instance.fetch_test()
test_instance.update_test()
test_instance.delete_test()
