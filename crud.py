from sqlalchemy.orm import Session
from database import JoueurDB, EquipeDB
from models import JoueurCreate, JoueurUpdate, EquipeCreate, EquipeUpdate
from typing import List, Optional


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


def get_joueur(db: Session, joueur_id: int):
    return db.query(JoueurDB).filter(JoueurDB.id == joueur_id).first()


def get_joueurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(JoueurDB).offset(skip).limit(limit).all()


def get_joueurs_by_equipe(db: Session, equipe_id: int):
    return db.query(JoueurDB).filter(JoueurDB.equipe_id == equipe_id).all()


def create_joueur(db: Session, joueur: JoueurCreate):
    db_joueur = JoueurDB(**joueur.dict())
    db.add(db_joueur)
    db.commit()
    db.refresh(db_joueur)
    return db_joueur


def update_joueur(db: Session, joueur_id: int, joueur: JoueurUpdate):
    db_joueur = db.query(JoueurDB).filter(JoueurDB.id == joueur_id).first()
    if db_joueur:
        update_data = joueur.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_joueur, field, value)
        db.commit()
        db.refresh(db_joueur)
    return db_joueur


def delete_joueur(db: Session, joueur_id: int):
    db_joueur = db.query(JoueurDB).filter(JoueurDB.id == joueur_id).first()
    if db_joueur:
        db.delete(db_joueur)
        db.commit()
    return db_joueur


def transfer_joueur(db: Session, joueur_id: int, nouvelle_equipe_id: int):
    db_joueur = db.query(JoueurDB).filter(JoueurDB.id == joueur_id).first()
    if db_joueur:
        db_joueur.equipe_id = nouvelle_equipe_id
        db.commit()
        db.refresh(db_joueur)
    return db_joueur 