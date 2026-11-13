from fastapi import FastAPI

from database import Base, engine
from routers import plataformas, jogos, avaliacoes

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Loja de Games API",
    description="API para gerenciamento de plataformas, jogos e avaliações.",
    version="1.0.0"
)

# Registrar rotas
app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)


@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo à API da Loja de Games!",
        "documentacao": "/docs"
    }