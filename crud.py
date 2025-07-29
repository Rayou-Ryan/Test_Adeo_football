from sqlalchemy.orm import Session
from database import EquipeDB
from models import EquipeCreate, EquipeUpdate


def get_equipe(db: Session, equipe_id: int):
    return db.query(EquipeDB).filter(EquipeDB.id == equipe_id).first()


def get_equipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EquipeDB).offset(skip).limit(limit).all()


def create_equipe(db: Session, equipe: EquipeCreate):
    db_equipe = EquipeDB(**equipe.dict())
    db.add(db_equipe)
    db.commit()
    db.refresh(db_equipe)
    return db_equipe


def update_equipe(db: Session, equipe_id: int, equipe: EquipeUpdate):
    db_equipe = db.query(EquipeDB).filter(EquipeDB.id == equipe_id).first()
    if db_equipe:
        update_data = equipe.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_equipe, field, value)
        db.commit()
        db.refresh(db_equipe)
    return db_equipe


def delete_equipe(db: Session, equipe_id: int):
    db_equipe = db.query(EquipeDB).filter(EquipeDB.id == equipe_id).first()
    if db_equipe:
        db.delete(db_equipe)
        db.commit()
    return db_equipe 