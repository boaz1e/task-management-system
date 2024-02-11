# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

MYSQL_DATABASE_URL = f"mysql+mysqlconnector://root:12345@127.0.0.1:3306/task-management-db"

engine = create_engine(MYSQL_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
