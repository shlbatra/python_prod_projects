from config import get_settings
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    get_settings().database_url, connect_args={"check_same_thread": False} # SQLite by default only allows one thread to access it - Remove this for PostgreSQL/MySQL
) # The engine is the starting point for SQLAlchemy - it manages the connection pool to your database


# SessionLocal isn't a session itself - it's a class that creates sessions. Each request gets its own session instance
# A session is a "workspace" for your database operations. It tracks changes, handles transactions, and executes queries

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Ensure tables are created
Base.metadata.create_all(bind=engine)

# FastAPI dependency generator 
# Code before yield runs before the request
# Code after yield (in finally) runs after the request completes
# Guarantees cleanup even if the route throws an exception

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()