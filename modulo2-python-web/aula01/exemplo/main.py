from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Criar a instancia da aplicação
app = FastAPI(
    title='API de Cadastro -- SENAI',
    description='Primeira API do curso de DS',
    version='0.1.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # Em produção, especificar o dominio do front
    allow_methods=['*'],
    allow_headers=['*'],
)

# Rota raiz -- GET /
@app.get('/')
def raiz():
    return {'mensagem': 'API funcionando!', 'versao': '0.1.0'}

# Rota de status -- GET /status
@app.get('/status')
def status():
    return {'status': 'online', 'servico': 'API SENAI'}

# Lista simulada de usuarios --  substitui o banco por enquanto
usuarios_db = [
    {'id': 1, 'nome': 'Max Muller', 'cargo': 'DEV', 'ativo': True},
    {'id': 2, 'nome': 'Alice Lima', 'cargo': 'Design', 'ativo': True},
    {'id': 3, 'nome': 'Carlos Silva', 'cargo': 'QA', 'ativo': False},
]

# GET /usuarios - retorna todos os usuarios
@app.get('/usuarios')
def listar_usuarios():
    return usuarios_db



@app.get('/usuarios/busca')
def buscar_por_nome(nome: str = ''):
    if not nome:
        return usuarios_db
    filtrados = [u for u in usuarios_db if nome.lower() in u ['nome'].lower()]
    return filtrados

@app.get('/usuario/ativos')
def listar_ativos():
    return [u for u in usuarios_db if u['ativo']]



@app.get('/usuarios/inativos')
def listar_inativos():
    return [u for u in usuarios_db if not u['ativo']]

@app.get('/usuarios/cargo/{cargo}')
def buscar_por_cargo(cargo: str):
        return[
            u for u in usuarios_db
            if cargo.lower() in u['cargo'].lower()
        ]

@app.get('/info')
def info_geral():
    return {
        'ttal_usuarios': len(usuarios_db), 
        'ativos': sum(1 for u in usuarios_db if u['atvos']),
        'inativos': sum(1 for u in usuarios_db if not u['ativo']),
    }

# GET /usuarios/(id) - retorna um usuario pelo ID
# O (id) é um path parameter - FastAPI extrai da URL automaticamente
@app.get('/usuarios/{usuario_id}')
def buscar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario['id'] == usuario_id:
            return usuario
    return {'erro': 'Usuario nao encontrado'}