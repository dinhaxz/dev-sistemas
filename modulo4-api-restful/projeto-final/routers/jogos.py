from fastapi import APIRouter, Depends, HTTPException
from models import Jogo, Plataforma, Avaliacao
from tags import AvaliacaoResponse
from sqlalchemy.orm import Session

from database import get_db
from models import Jogo, Plataforma
from tags import (
    JogoCreate,
    JogoResponse,
    TAG_JOGOS
)

router = APIRouter(
    prefix="/jogos",
    tags=TAG_JOGOS
)


@router.get("/", response_model=list[JogoResponse])
def listar_jogos(db: Session = Depends(get_db)):
    return db.query(Jogo).all()


@router.get("/{id}", response_model=JogoResponse)
def buscar_jogo(id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado"
        )

    return jogo


@router.post("/", response_model=JogoResponse, status_code=201)
def cadastrar_jogo(
    jogo: JogoCreate,
    db: Session = Depends(get_db)
):
    plataforma = db.query(Plataforma).filter(
        Plataforma.id == jogo.plataforma_id
    ).first()

    if not plataforma:
        raise HTTPException(
            status_code=404,
            detail="Plataforma não encontrada"
        )

    novo_jogo = Jogo(
        titulo=jogo.titulo,
        genero=jogo.genero,
        preco=jogo.preco,
        plataforma_id=jogo.plataforma_id
    )

    db.add(novo_jogo)
    db.commit()
    db.refresh(novo_jogo)

    return novo_jogo


@router.put("/{id}", response_model=JogoResponse)
def atualizar_jogo(
    id: int,
    dados: JogoCreate,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado"
        )

    plataforma = db.query(Plataforma).filter(
        Plataforma.id == dados.plataforma_id
    ).first()

    if not plataforma:
        raise HTTPException(
            status_code=404,
            detail="Plataforma não encontrada"
        )

    jogo.titulo = dados.titulo
    jogo.genero = dados.genero
    jogo.preco = dados.preco
    jogo.plataforma_id = dados.plataforma_id

    db.commit()
    db.refresh(jogo)

    return jogo


@router.delete("/{id}")
def remover_jogo(id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado"
        )

    db.delete(jogo)
    db.commit()

    return {"mensagem": "Jogo removido com sucesso"}

@router.get(
    "/{id}/avaliacoes",
    response_model=list[AvaliacaoResponse]
)
def listar_avaliacoes_do_jogo(
    id: int,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado"
        )

    return db.query(Avaliacao).filter(
        Avaliacao.jogo_id == id
    ).all()