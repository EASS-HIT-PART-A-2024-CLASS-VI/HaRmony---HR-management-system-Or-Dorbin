from sqlalchemy import create_engine, inspect
from app import models

# Create an in-memory SQLite database
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})

# Create tables
models.Base.metadata.create_all(bind=engine)

# Check existing tables
inspector = inspect(engine)
print("Existing Tables:", inspector.get_table_names())  # Should list all tables
