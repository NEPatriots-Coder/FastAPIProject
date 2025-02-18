import pytest
import sys
import os
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import Base

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


print("Current working directory:", os.getcwd())
project_root = Path(__file__).parent.parent
print("Project root:", project_root)
print("Python path before:", sys.path)
print("Python path after:", sys.path)
print("Contents of app directory:", os.listdir(project_root / "app"))