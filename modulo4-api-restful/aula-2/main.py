from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, Base, get_db
from models import Usuario
from schemas import UsuarioCreate, UsuarioPatch, UsuarioResponse, ErroResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='API de Usuários',
    description='Demonstração de validação avançada com Pydantic',
    version='1.0.0'
)

# GET / - Página inicial da API
@app.get('/')
def home():
    return {
        'mensagem': 'API de Usuários funcionando!',
        'documentacao': '/docs',
        'rotas': {
            'cadastrar_usuario': 'POST /usuarios',
            'listar_usuarios': 'GET /usuarios',
            'buscar_usuario': 'GET /usuarios/{usuario_id}',
            'atualizar_usuario': 'PATCH /usuarios/{usuario_id}',
            'remover_usuario': 'DELETE /usuarios/{usuario_id}'
        }
    }


# POST /usuarios - Cadastrar novo usuário
# A resposta não expõe a senha, graças ao UsuarioResponse.
@app.post(
    '/usuarios',
    response_model=UsuarioResponse,
    status_code=201,
    responses={409: {'model': ErroResponse}}
)
def criar_usuario(dados: UsuarioCreate, db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter(
        Usuario.email == dados.email
    ).first()

    if existe:
        raise HTTPException(
            status_code=409,
            detail='E-mail já cadastrado'
        )

    # Para estudo. Em produção, armazene somente uma senha com hash seguro.
    usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        hash_senha=dados.senha
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


# GET /usuarios - Listar todos os usuários ativos
@app.get('/usuarios', response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.ativo == True).all()


# GET /usuarios/{id} - Buscar usuário por ID
@app.get('/usuarios/{usuario_id}', response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario or not usuario.ativo:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado'
        )

    return usuario


# PATCH /usuarios/{id} - Atualizar parcialmente
@app.patch('/usuarios/{usuario_id}', response_model=UsuarioResponse)
def atualizar_usuario(
    usuario_id: int,
    dados: UsuarioPatch,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario or not usuario.ativo:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado'
        )

    if dados.email and dados.email != usuario.email:
        existe = db.query(Usuario).filter(
            Usuario.email == dados.email
        ).first()

        if existe:
            raise HTTPException(
                status_code=409,
                detail='E-mail já em uso'
            )

    if dados.nome is not None:
        usuario.nome = dados.nome

    if dados.email is not None:
        usuario.email = dados.email

    db.commit()
    db.refresh(usuario)

    return usuario


# DELETE /usuarios/{id} - Remover usuário logicamente
@app.delete('/usuarios/{usuario_id}')
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario or not usuario.ativo:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado'
        )

    usuario.ativo = False
    db.commit()

    return {
        'mensagem': f'Usuário {usuario_id} removido'
    }
