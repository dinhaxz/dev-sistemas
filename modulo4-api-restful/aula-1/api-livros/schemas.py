
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LivroCreate(BaseModel):
    titulo: str = Field(min_length=2, max_length=200)
    autor: str = Field(min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None
    disponivel: bool = True


class LivroUpdate(BaseModel):
    titulo: Optional[str] = Field(
        default=None, min_length=2, max_length=200
    )
    autor: Optional[str] = Field(
        default=None, min_length=2, max_length=150
    )
    ano_publicacao: Optional[int] = None
    disponivel: Optional[bool] = None


class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: Optional[int]
    disponivel: bool
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)
