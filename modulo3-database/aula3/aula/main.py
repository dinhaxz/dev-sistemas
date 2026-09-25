from sqlalchemy import Column, Integer, String, Boolean, text
from app.database import engine, Base, SessionLocal

# modelo (tabela) diretamente
class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    sigla = Column(String(150), nullable=False)
    ativo = Column(Boolean, default=True)

# criar tabela
Base.metadata.create_all(bind=engine)
print('create table')

# inserir dados
db = SessionLocal()
try:

    # verificar se ja tem dados:
    if db.query(Departamento).count() == 0:
        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM')
        ])
    db.commit()
    print("dados inseridos")

    departamentos = db.query(Departamento).order_by(Departamento.nome).all()
    print(f'\n{len(departamentos)} Departamentos no banco')
    for departamento in departamentos:
        print(f"{departamento.id}: {departamento.nome} ({departamento.sigla})")


finally:
    db.close()