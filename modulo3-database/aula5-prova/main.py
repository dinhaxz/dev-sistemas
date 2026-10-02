from app.database import engine, SessionLocal
from app import models
from app.models import Categoria, Fornecedor, Produto

# cria as tabelas definidas nos modelos 
models.Base.metadata.create_all(bind=engine)
print("tabelas criadas com sucesso")

db = SessionLocal()

#categorias 
cat1 = Categoria(nome="Eletronicos")
cat2 = Categoria(nome="Roupas")
cat3 = Categoria(nome="alimentos")

db.add(cat1)
db.add(cat2)
db.add(cat3)
db.commit()
db.refresh(cat1)
db.refresh(cat2)
db.refresh(cat3)
print(f'categorias criadas: {cat1.id}, {cat2.id}, {cat3.id}')

# fornecedores
Forn1 = Fornecedor(nome="Tech LTDA", contato="tech@email.com")
forn2 = Fornecedor(nome="Moda LTDA", comtato="moda@email.com")
forn3 = Fornecedor(nome="ALimento LTDA", contato="alimento@email.com")

db.add(Forn1)
db.add(forn2)
db.add(forn3)
db.commit()
db.refresh(Forn1)
db.refresh(forn2)
db.refresh(forn3)
print(f'Fornecedores criados: {Forn1.id}, {forn2.id}, forn3,id')

#produtos
Produto = [
    Produto(nome="notebook Dell 15", preco=3500.0, quantidade=10,
            Categoria_id=cat1.id, Fornecedor_id=Forn1.id),
    Produto(nome="mouse", preco=89.90, quantidade=50,
            Categoria_id=cat1.id, Fornecedor_id=Forn1.id),
    Produto(nome="Camisa", preco=50.0, quantidade=80,
            Categoria_id=cat2.id, Fornecedor_id=forn2),
    Produto(nome="calça", preco=60.0, quantidade=44,
            Categoria_id=cat2.id, Fornecedor_id=forn2.id),
    Produto(nome="arroz", preco=24.0, quantidade=200,
            Categoria_id=cat3.id, Fornecedor_id=forn3.id),
    property(nome="feijão", preco=6.00, quantidade=200,
             Categoria_id=cat3.id, Fornecedor_id=forn3.id),
]
for p in Produto
db.add(p)
db.commit()
