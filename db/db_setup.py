from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./sql_app.db'
# SQLALCHEMY_DATABASE_URL: str = 'postgresql+psycopg2://user:password@postgresserver/db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        'check_same_thread': False # Commented
    }, # future=True
)

SessionLocal = sessionmaker(
    bind=engine, autoflush=False,
    autocommit=False, # future=True
)

_Base = declarative_base()
