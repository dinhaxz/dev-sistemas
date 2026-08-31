from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional

app = FastAPI()


# Modelo para criar usuário
class Usuario(BaseModel):
    nome: str
    idade: int
    cargo: str
    salario: Optional[float] = None
    ativo: bool = True

    # Validador de cargo
    @field_validator("cargo")
    @classmethod
    def validar_cargo(cls, v):
        cargos_aceitos = [
            "Desenvolvedor",
            "Designer",
            "QA",
            "Product Manager"
        ]

        if v not in cargos_aceitos:
            raise ValueError("Cargo não permitido")

        return v

    # Exercício 2 - Validador de salário
    @field_validator("salario")
    @classmethod
    def validar_salario(cls, v):
        if v is None:
            return v

        if v <= 0:
            raise ValueError("O salário deve ser maior que zero")

        return v


# Modelo de resposta
class UsuarioResposta(BaseModel):
    id: int
    nome: str
    idade: int
    cargo: str
    salario: Optional[float] = None
    ativo: bool


# Banco de dados temporário
usuarios_db = [
    {
        "id": 1,
        "nome": "Ana",
        "idade": 25,
        "cargo": "Desenvolvedor",
        "salario": 5000,
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Bruno",
        "idade": 30,
        "cargo": "Designer",
        "salario": 4500,
        "ativo": True
    },
    {
        "id": 3,
        "nome": "Carlos",
        "idade": 28,
        "cargo": "QA",
        "salario": 4000,
        "ativo": False
    }
]


# Exercício 1
proximo_id = 4


# Rota inicial
@app.get("/")
def inicio():
    return {"mensagem": "API de usuários funcionando!"}


# Lista todos os usuários
@app.get("/usuarios", response_model=list[UsuarioResposta])
def listar_usuarios():
    return usuarios_db


# Exercício 3 - Lista somente usuários ativos
# DEVE FICAR ANTES de /usuarios/{usuario_id}
@app.get("/usuarios/ativos", response_model=list[UsuarioResposta])
def listar_ativos():
    return [u for u in usuarios_db if u["ativo"]]


# Exercício 4 - Filtra usuários por cargo
# DEVE FICAR ANTES de /usuarios/{usuario_id}
@app.get("/usuarios/cargo/{cargo}", response_model=list[UsuarioResposta])
def listar_por_cargo(cargo: str):
    return [
        u for u in usuarios_db
        if u["cargo"].lower() == cargo.lower()
    ]


# Busca usuário pelo ID
@app.get("/usuarios/{usuario_id}", response_model=UsuarioResposta)
def buscar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario["id"] == usuario_id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )


# Exercício 1 - Adiciona novo usuário
@app.post("/usuarios", response_model=UsuarioResposta)
def criar_usuario(usuario: Usuario):
    global proximo_id

    novo_usuario = {
        "id": proximo_id,
        **usuario.model_dump()
    }

    usuarios_db.append(novo_usuario)
    proximo_id += 1

    return novo_usuario


# Exercício 5 - Informações da API
@app.get("/info", tags=["Geral"])
def info():
    total = len(usuarios_db)

    ativos = len([
        u for u in usuarios_db
        if u["ativo"]
    ])

    return {
        "total_usuarios": total,
        "usuarios_ativos": ativos,
        "cargos_aceitos": [
            "Desenvolvedor",
            "Designer",
            "QA",
            "Product Manager"
        ]
    }