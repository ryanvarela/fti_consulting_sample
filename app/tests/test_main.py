from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FTI Consulting Data API."}

def test_get_intraday_unauthorized():
    response = client.get("/intraday/IBM")
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate API key."}

def test_get_intraday_authorized():
    headers = {"X-API-KEY": "mysecureapikey"}
    response = client.get("/intraday/IBM", headers=headers)
    assert response.status_code == 200
    assert "Time Series (5min)" in response.json()
