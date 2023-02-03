from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings


from typing import Generator
# using postgre SQL

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#to connect uing SQLALCHEMY

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}

)

essionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


#dependency injection for database 

def get_db() -> Generator:
    try:
        db=sessionLocal()
        yield db
    finally:
        db.close()