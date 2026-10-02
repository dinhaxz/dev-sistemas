from app.database import engine, SessionLocal, Base
from app import models


# Criação das tabelas
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")


# Criação da sessão
db = SessionLocal()

try:
    # ==========================================
    # 1. GÊNEROS
    # ==========================================

    genero1 = models.Genero(nome="Ficção")
    genero2 = models.Genero(nome="Romance")
    genero3 = models.Genero(nome="Fantasia")

    db.add_all([genero1, genero2, genero3])
    db.commit()

    print("Gêneros inseridos com sucesso!")


    # ==========================================
    # 2. AUTORES
    # ==========================================

    autor1 = models.Autor(
        nome="Machado de Assis",
        nacionalidade="Brasileira"
    )

    autor2 = models.Autor(
        nome="J. K. Rowling",
        nacionalidade="Britânica"
    )

    autor3 = models.Autor(
        nome="Gabriel García Márquez",
        nacionalidade="Colombiana"
    )

    db.add_all([autor1, autor2, autor3])
    db.commit()

    print("Autores inseridos com sucesso!")


    # ==========================================
    # 3. LIVROS
    # ==========================================

    livro1 = models.Livro(
        titulo="Dom Casmurro",
        ano_publicacao=1899,
        disponivel=True,
        genero_id=genero1.id,
        autor_id=autor1.id
    )

    livro2 = models.Livro(
        titulo="Memórias Póstumas de Brás Cubas",
        ano_publicacao=1881,
        disponivel=True,
        genero_id=genero1.id,
        autor_id=autor1.id
    )

    livro3 = models.Livro(
        titulo="Harry Potter e a Pedra Filosofal",
        ano_publicacao=1997,
        disponivel=True,
        genero_id=genero3.id,
        autor_id=autor2.id
    )

    livro4 = models.Livro(
        titulo="Harry Potter e a Câmara Secreta",
        ano_publicacao=1998,
        disponivel=False,
        genero_id=genero3.id,
        autor_id=autor2.id
    )

    livro5 = models.Livro(
        titulo="Cem Anos de Solidão",
        ano_publicacao=1967,
        disponivel=True,
        genero_id=genero2.id,
        autor_id=autor3.id
    )

    db.add_all([livro1, livro2, livro3, livro4, livro5])
    db.commit()

    print("Livros inseridos com sucesso!")
    print("Banco de dados populado com sucesso!")

finally:
    db.close()
