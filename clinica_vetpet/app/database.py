import os
os.environ["DISABLE_SQLALCHEMY"] = "1"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL do banco SQLite - Cria o arquivo estoque.db na raiz do projeto
DATABASE_URL = "sqlite:///./clinica_vetpet.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass