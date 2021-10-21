from starlette.testclient import TestClient
from modelwatch_app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
