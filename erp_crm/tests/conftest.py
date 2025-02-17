# test/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app
from app.config import settings

# Test database URL
TEST_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def test_engine():
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def test_db(test_engine):
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=test_engine
    )
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


# test/test_auth.py
def test_create_user(test_client, test_db):
    response = test_client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "testpassword123",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "password" not in data


def test_login_user(test_client, test_db):
    # First create a user
    test_client.post(
        "/api/auth/register",
        json={
            "email": "login@example.com",
            "password": "testpassword123",
            "full_name": "Login Test"
        }
    )

    # Then try to login
    response = test_client.post(
        "/api/auth/token",
        data={
            "username": "login@example.com",
            "password": "testpassword123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


# test/test_customers.py
def test_create_customer(test_client, test_db, auth_headers):
    response = test_client.post(
        "/api/customers/",
        headers=auth_headers,
        json={
            "company_name": "Test Company",
            "industry": "Technology",
            "address": "123 Test St"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["company_name"] == "Test Company"