from app.database import SessionLocal
from app.models import Curso, Aluno

def popular_banco():
    db = SessionLocal()
    try:
        if db.query(Curso).count() > 0:
            print("Banco já populado. Pulando...")
            return
            
        # Inserir cursos
        db.add_all([
            Curso(nome='Cybersecurity', duracao=1200),
            Curso(nome='Network', duracao=1000),
            Curso(nome='Cloud', duracao=1400)
        ])
        
        # Inserir alunos
        db.add_all([
            Aluno(nome='Baby', email='baby@gmail.com', matricula='2025001'),
            Aluno(nome='Dinha', email='dinha@gmail.com', matricula='2025002'),
            Aluno(nome='Toin', email='carlos@gmail.com', matricula='2025003'),
            Aluno(nome='Bea', email='bea@gmail.com', matricula='2025004')
        ])
        
        db.commit()
        print('Banco populado com sucesso!')
        
    except Exception as e:
        db.rollback()
        print(f'Erro: {e}')
    finally:
        db.close()

if __name__ == '__main__':
    popular_banco()