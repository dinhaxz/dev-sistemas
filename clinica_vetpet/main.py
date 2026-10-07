from app.database import Base, engine, SessionLocal
from app.crud import(
    inserir_tutor,
    inserir_animal,
    inserir_atendimento
)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

#tutores
inserir_tutor(
    db,
    "toin",
    "6767676766",
    "toin67@gmail.com"
)

inserir_tutor(
    db,
    "mariduanus",
    "1234567890",
    "maridu67@gmail.com"
)

print("tutores inserids com sucesso")

#animais
inserir_animal(
    db,
    "nina",
    "cachorra",
    "caramelo",
    25.5,
    1
)

inserir_animal(
    db,
    "nico",
    "gato",
    "Siamês",
    4.2,
    2
)

print("animais inseridos com sucesso")

#atendimento
inserir_atendimento(
    db,
    "07/10/2026",
    "consulta de rotina",
    80.00,
    1
)

inserir_atendimento(
    db,
    "06/10/2026",
    "tosa",
    50.00,
    1
)

print("atendimento inseridos com sucesso")
print("sistemas executado com sucesso")

db.close()