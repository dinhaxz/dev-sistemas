from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import usuarios 

app = FastAPI(
    title= 'API de cadastro - SENAI',
    version= '0.3.0'
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

# resgistrar o router - inclui todas as rotas de usarios.py
app.include_router(usuarios.router)

#rotas raiz permanece aqui 
@app.get('/', tags=['Geral'])
def raiz():
    return {'status': 'online', 'versão': '0.3.0'}
