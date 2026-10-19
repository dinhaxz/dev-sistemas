
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from models import Livro
from schemas import LivroCreate, LivroResponse, LivroUpdate

router = APIRouter(prefix="/livros", tags=["Livros"])


@router.get("/", response_model=list[LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return (
        db.query(Livro)
        .filter(Livro.disponivel.is_(True))
        .order_by(Livro.id)
        .all()
    )


@router.get("/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()

    if livro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )

    return livro


@router.post(
    "/",
    response_model=LivroResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_livro(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(**dados.model_dump())

    db.add(livro)
    db.commit()
    db.refresh(livro)

    return livro


@router.patch("/{livro_id}", response_model=LivroResponse)
def atualizar_livro(
    livro_id: int,
    dados: LivroUpdate,
    db: Session = Depends(get_db)
):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()

    if livro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )

    alteracoes = dados.model_dump(exclude_unset=True)

    for campo, valor in alteracoes.items():
        setattr(livro, campo, valor)

    db.commit()
    db.refresh(livro)

    return livro


@router.delete("/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()

    if livro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )

    livro.disponivel = False

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
