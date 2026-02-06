import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json == {"status": "OK", "version": "1.0"}

def test_list_servers(client):
    response = client.get('/api/v1/servers')
    assert response.status_code == 200
    data = response.json
    assert "servers" in data
    assert data["count"] == 2
    assert len(data["servers"]) == 2

def test_get_server_by_id(client):
    response = client.get('/api/v1/servers/1')
    assert response.status_code == 200
    data = response.json
    assert data["id"] == 1
    assert data["hostname"] == "web-prod-01"

def test_get_server_not_found(client):
    response = client.get('/api/v1/servers/999')
    assert response.status_code == 404
    assert response.json == {"error": "Server not found"}
