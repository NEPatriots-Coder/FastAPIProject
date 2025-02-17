# tests/test_auth.py
import pytest
from fastapi.testclient import TestClient

def test_user_registration(client, test_db):
    # Test data
    test_user = {
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }
    
    # Make request to register endpoint
    response = client.post("/api/auth/register", json=test_user)
    
    # Assert response
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user["email"]
    assert data["full_name"] == test_user["full_name"]
    assert "password" not in data  # Ensure password is not in response