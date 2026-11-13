from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Plataforma
from tags import (
    PlataformaCreate,
    PlataformaResponse,
    TAG_PLATAFORMAS
)

router = APIRouter(
    prefix="/plataformas",
    tags=TAG_PLATAFORMAS
)


@router.get("/", response_model=list[PlataformaResponse])
def listar_plataformas(db: Session = Depends(get_db)):
    return db.query(Plataforma).all()


@router.post("/", response_model=PlataformaResponse, status_code=201)
def cadastrar_plataforma(
    plataforma: PlataformaCreate,
    db: Session = Depends(get_db)
):
    nova_plataforma = Plataforma(nome=plataforma.nome)

    db.add(nova_plataforma)
    db.commit()
    db.refresh(nova_plataforma)

    return nova_plataforma