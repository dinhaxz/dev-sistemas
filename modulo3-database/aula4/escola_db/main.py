from app.database import engine, Base
from app import models
from app.seed import popular_banco

# Criar todas as tabelas que não existem no banco de dados
Base.metadata.create_all(bind=engine)

# Chamar a função para inserir os dados iniciais (seed)
popular_banco()