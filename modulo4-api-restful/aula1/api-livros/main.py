
from fastapi import FastAPI

from database import Base, engine
from models import Livro
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Livros API",
    description="API de cadastro e gerenciamento de livros com SQLite",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"mensagem": "API de livros funcionando!"}
