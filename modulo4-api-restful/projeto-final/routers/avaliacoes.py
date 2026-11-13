from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Avaliacao, Jogo
from tags import (
    AvaliacaoCreate,
    AvaliacaoResponse,
    TAG_AVALIACOES
)

router = APIRouter(
    prefix="/avaliacoes",
    tags=TAG_AVALIACOES
)


@router.post(
    "/",
    response_model=AvaliacaoResponse,
    status_code=201
)
def registrar_avaliacao(
    avaliacao: AvaliacaoCreate,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(
        Jogo.id == avaliacao.jogo_id
    ).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado"
        )

    nova_avaliacao = Avaliacao(
        nota=avaliacao.nota,
        comentario=avaliacao.comentario,
        jogo_id=avaliacao.jogo_id
    )

    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)

    return nova_avaliacao


@router.get(
    "/{jogo_id}/avaliacoes",
    response_model=list[AvaliacaoResponse]
)
def listar_avaliacoes(
    jogo_id: int,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(
        Jogo.id == jogo_id
    ).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado"
        )

    return db.query(Avaliacao).filter(
        Avaliacao.jogo_id == jogo_id
    ).all()


@router.delete("/{id}")
def remover_avaliacao(
    id: int,
    db: Session = Depends(get_db)
):
    avaliacao = db.query(Avaliacao).filter(
        Avaliacao.id == id
    ).first()

    if not avaliacao:
        raise HTTPException(
            status_code=404,
            detail="Avaliação não encontrada"
        )

    db.delete(avaliacao)
    db.commit()

    return {"mensagem": "Avaliação removida com sucesso"}