
from datetime import datetime
from typing import Optional
import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class UsuarioCreate(BaseModel):
    nome: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nome do usuário, entre 2 e 100 caracteres"
    )
    email: EmailStr
    senha: str = Field(
        ...,
        min_length=8,
        description="Senha com pelo menos 8 caracteres, uma letra e um número"
    )

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("O nome não pode conter apenas espaços.")

        if len(valor) < 2 or len(valor) > 100:
            raise ValueError("O nome deve ter entre 2 e 100 caracteres.")

        if any(char.isdigit() for char in valor):
            raise ValueError("O nome não pode conter números.")

        return valor

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, valor: str) -> str:
        if not any(char.isalpha() for char in valor):
            raise ValueError("A senha deve conter pelo menos uma letra.")

        if not any(char.isdigit() for char in valor):
            raise ValueError("A senha deve conter pelo menos um número.")

        return valor


class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100,
        description="Nome opcional do usuário"
    )
    email: Optional[EmailStr] = None

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: Optional[str]) -> Optional[str]:
        if valor is None:
            return None

        valor = valor.strip()

        if not valor:
            raise ValueError("O nome não pode conter apenas espaços.")

        if len(valor) < 2 or len(valor) > 100:
            raise ValueError("O nome deve ter entre 2 e 100 caracteres.")

        if any(char.isdigit() for char in valor):
            raise ValueError("O nome não pode conter números.")

        return valor


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True


class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None
