# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config


MYSQL_DATABASE_URL = "mysql+mysqlconnector://user:password@mysql-db:3306/db"

engine = create_engine(MYSQL_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()