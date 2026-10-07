from app.models import Tutor, Animal, Atendimento

def inserir_tutor(db, nome_completo, telefone, email):
    tutor = Tutor(
        nome_completo=nome_completo,
        telefone=telefone,
        email=email
    )
    db.add(tutor)
    db.commit()
    db.refresh(tutor)
    return tutor

def inserir_animal(db, nome_animal, especie, raca, peso_kg, tutor_id):
    animal = Animal(
        nome_completo=nome_animal,
        especie=especie,
        raca=raca,
        peso_kg=peso_kg,
        tutor_id=tutor_id
    )
    db.add(animal)
    db.commit()
    db.refresh(animal)
    return animal

def inserir_atendimento(db, data_atend, motivo, valor_cons, animal_id):
    atendimento = Atendimento(
        data_atend=data_atend,
        motivo=motivo,
        valor_cons=valor_cons,
        animal_id=animal_id
    )
    db.add(atendimento)
    db.commit()
    db.refresh(atendimento)
    return atendimento