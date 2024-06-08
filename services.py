from sqlalchemy.orm import Session
import db.models as models
import schemas

def create_juiz(db: Session, juiz: schemas.JuizCreate):
    db_juiz = models.Juiz(full_name=juiz.full_name)
    db.add(db_juiz)
    db.commit()
    db.refresh(db_juiz)
    return db_juiz

def get_juiz(db: Session, juiz_id: int):
    return db.query(models.Juiz).filter(models.Juiz.id==juiz_id).first()

def create_sentenciado(db: Session, sentenciado: schemas.SentenciadoCreate):
    db_sentenciado = models.Sentenciado(
        name=sentenciado.name,
        felony=sentenciado.felony,
        sentence=sentenciado.sentence
    )
    db.add(db_sentenciado)
    db.commit()
    db.refresh(db_sentenciado)
    return db_sentenciado

def get_sentenciado(db: Session, sentenciado_id: int):
    return db.query(models.Sentenciado).filter(models.Sentenciado.id==sentenciado_id).first()

def get_sentenciados(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Sentenciado).offset(skip).limit(limit).all()

def update_sentenciado(db: Session, sentenciado_id: int, sentenciado_update: schemas.SentenciadoCreate):
    db_sentenciado = db.query(models.Sentenciado).filter(models.Sentenciado.id==sentenciado_id).first()
    if db_sentenciado is None:
        return None
    db_sentenciado.name = sentenciado_update.name
    db_sentenciado.felony = sentenciado_update.felony
    db_sentenciado.sentence = sentenciado_update.sentence
    db.commit()
    db.refresh(db_sentenciado)
    return db_sentenciado

def delete_sentenciado(db: Session, sentenciado_id: int):
    db_sentenciado = db.query(models.Sentenciado).filter(models.Sentenciado.id == sentenciado_id).first()
    if db_sentenciado is None:
        return None
    db.delete(db_sentenciado)
    db.commit()
    return db_sentenciado