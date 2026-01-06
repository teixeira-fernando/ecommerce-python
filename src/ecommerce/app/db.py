import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:55432/ecommerce_db"
)

Base = declarative_base()
metadata = MetaData()

# SQLAlchemy engine (sync, for migrations)
engine = create_engine(
    DATABASE_URL.replace("+asyncpg", ""),
    echo=True
)

# SessionLocal for sync operations (e.g., Alembic)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Async database for FastAPI
database = Database(DATABASE_URL)