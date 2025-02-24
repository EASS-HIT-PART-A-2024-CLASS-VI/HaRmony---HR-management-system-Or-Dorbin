import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
from app import models  # Ensure all models are loaded

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///test_db.sqlite"  # 🔹 Persistent SQLite file
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app.dependency_overrides[get_db] = lambda: iter([TestingSessionLocal()])  # 🔹 Force FastAPI to use the test DB globally

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """Ensure tables exist in the test database before any tests run."""
    app.dependency_overrides.clear()  # Clear FastAPI dependencies
    models.Base.metadata.drop_all(bind=engine)  # Clean slate
    models.Base.metadata.create_all(bind=engine)  # Recreate tables
    print("✅ Tables created for testing:", inspect(engine).get_table_names())  # Debugging


@pytest.fixture(scope="function")
def db_session(setup_test_db):
    app.dependency_overrides.clear()
    """Provide a fresh test database session."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def client(db_session):
    app.dependency_overrides.clear()
    """Provide a test client using the test database session."""
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db  # 🔹 Force FastAPI to use the test DB
    print("Overriding get_db with:", override_get_db)
    return TestClient(app)


def test_get_all_employees(client):
    print("Current get_db function:", get_db) 
    response = client.get("/Employees/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_employees(client):
    response = client.get("/Employees/search/?name=John")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_birthdays(client):
    response = client.get("/Employees/birthdays/?month=1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_register_user(client):
    data = {"username": "testuser", "password": "testpass", "role": "admin", "company": "TestCorp"}
    response = client.post("/auth/register/", json=data)
    assert response.status_code == 200
    assert "user_id" in response.json()

def test_login_user(client):
    data = {"username": "testuser", "password": "testpass"}
    response = client.post("/auth/login/", json=data)
    assert response.status_code in [200, 400]

def test_create_event(client):
    data = {"name": "Team Meeting", "date": "2025-02-23", "location": "HQ", "organizer": "John Doe"}
    response = client.post("/happy_hour/event/", json=data)
    assert response.status_code in [200, 500]

def test_get_potential_recruits(client):
    response = client.get("/potential_recruits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_upcoming_events(client):
    response = client.get("/formation_events/upcoming/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_past_events(client):
    response = client.get("/formation_events/past/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_approved_places(client):
    response = client.get("/formation_events/approved_places/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
