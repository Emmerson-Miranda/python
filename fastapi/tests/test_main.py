from app import main
from fastapi.testclient import TestClient

client = TestClient(main.server)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_addition_item():
    response = client.post("/addition/", json={"x": "4", "y": "3"})
    assert response.status_code == 200
    assert response.json() == {"x": 4, "y": 3, "result": 7}
