from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import Response

app = FastAPI(title='API de cadastro - SENAI', version='0.2.0')

# modelo pydantic: define a estrurura e os tipos 
#receber informaççoes 
class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True #valor padrão
    salario: Optional[float] = None # campo opcional 

    @field_validator('nome')
    @classmethod 
    def validar_nome(cls, v):
            v = v.strip()
            if len(v) < 3:
                raise ValueError('Nome deve ter pelo menos 3 caracteres')
            return v.title() # nao errar o espaçamento 

# modelo resposta: incluir o ID gerado pelo servidor 
class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    ativo: bool
    salario: Optional[float] = None

usuario_db: list[UsuarioResposta] = [
    UsuarioResposta(id=1, nome='Toin jesus', email='toin@gmail.com',
                    cargo='Desing', ativo=True, salario=3800.0),

    UsuarioResposta(id=2, nome='Maros rodrigues', email='maros@gmail.com',
                    cargo='QA', ativo=True, salario=3200.0),

    UsuarioResposta(id=3, nome='Filipe farias', email='filipe@gmail.com',
                    cargo='Dev', ativo=True, salario=4500.0),
]
proximo_id = 4

# GET /usuarios - Lista todos os usuario 
@app.get('/usuarios', response_model=list[UsuarioResposta])
def listar_usuarios():
     return usuario_db

@app.get('/usuarios/{usuario_db}', response_model=UsuarioResposta)
def buscar_usuario(usario_id: int):
     for usuario in usuario_db:
        if usuario.id == usario_id:
            return usuario
        raise HTTPException(status_code=404, detail='Usuario nao encontrado ')

@app.post('/usuarios', response_model=UsuarioResposta, status_code=201)
def criar_usuario(dados: Usuario):
    global proximo_id
     # verificar e-mail duplicado
    for u in usuario_db:
          if u.email == dados.email:
               raise HTTPException(400, 'E-mail ja cadastrado')
    novo = UsuarioResposta(id=proximo_id, **dados.model_dump())
    usuario_db.append(novo)
    proximo_id += 1
    return novo

@app.put('/usuarios/{usuario_id}', response_model=UsuarioResposta)
def atualizar_usuario(usuario_id: int, dados: Usuario):
     for i, u in enumerate(usuario_db):
          if u.id == usuario_id:
               atualizado = UsuarioResposta(id=usuario_id, **dados.model_dump())
               usuario_db[i] = atualizado
               return atualizado
          raise HTTPException(404, 'Usuario não encontrado')

@app.delete('/usuarios/{usuario_id}', status_code=204)
def deletar_usuario(usuario_id: int):
     for i, u in enumerate(usuario_db):
          if u.id == usuario_id:
               usuario_db.pop(i)
               return Response(status_code=204)
          raise HTTPException(404, 'Usuarios nao encontrado')
     
     


          