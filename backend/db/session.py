from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# using postgre SQL

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#to connect uing SQLALCHEMY

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}

# )

sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

