from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

class Tutor(Base):
    __tablename__= "tutores"

    id= Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=False)

class Animal(Base):
    __tablename__= "animais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(60), nullable=False)
    especie = Column(String(40), nullable=False)
    raca = Column(String(60), nullable=True)
    peso_kg = Column(Float, nullable=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))

class Atendimento(Base):
    __tablename__= "atendimentos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_atend = Column(String(20), nullable=False)
    motivo = Column(String(200), nullable=True)
    valor_cons = Column(Float, nullable=False)
    animal_id = Column(Integer, ForeignKey("animais.id"))

