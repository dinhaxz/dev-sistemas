from pydantic import BaseModel, Field, ConfigDict


# PLATAFORMAS

class PlataformaCreate(BaseModel):
    nome: str


class PlataformaResponse(BaseModel):
    id: int
    nome: str

    model_config = ConfigDict(from_attributes=True)


# JOGOS

class JogoCreate(BaseModel):
    titulo: str
    genero: str
    preco: float
    plataforma_id: int


class JogoResponse(BaseModel):
    id: int
    titulo: str
    genero: str
    preco: float
    plataforma_id: int

    model_config = ConfigDict(from_attributes=True)


# AVALIACOES

class AvaliacaoCreate(BaseModel):
    nota: int = Field(ge=1, le=5)
    comentario: str
    jogo_id: int


class AvaliacaoResponse(BaseModel):
    id: int
    nota: int
    comentario: str
    jogo_id: int

    model_config = ConfigDict(from_attributes=True)


# TAGS DA DOCUMENTACAO

TAG_PLATAFORMAS = ["Plataformas"]
TAG_JOGOS = ["Jogos"]
TAG_AVALIACOES = ["Avaliações"]