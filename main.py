from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
from database import get_db, engine, Base
from models import (
    Joueur, JoueurCreate, JoueurUpdate,
    Equipe, EquipeCreate, EquipeUpdate
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Orchestrateur Football",
    description="API de gestion des joueurs et équipes de football",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'orchestrateur de football"}


@app.post("/equipes/", response_model=Equipe)
def create_equipe(equipe: EquipeCreate, db: Session = Depends(get_db)):
    return crud.create_equipe(db=db, equipe=equipe)


@app.get("/equipes/", response_model=List[Equipe])
def read_equipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipes = crud.get_equipes(db, skip=skip, limit=limit)
    return equipes


@app.get("/equipes/{equipe_id}", response_model=Equipe)
def read_equipe(equipe_id: int, db: Session = Depends(get_db)):
    db_equipe = crud.get_equipe(db, equipe_id=equipe_id)
    if db_equipe is None:
        raise HTTPException(status_code=404, detail="Équipe non trouvée")
    return db_equipe


@app.put("/equipes/{equipe_id}", response_model=Equipe)
def update_equipe(equipe_id: int, equipe: EquipeUpdate, db: Session = Depends(get_db)):
    db_equipe = crud.update_equipe(db, equipe_id=equipe_id, equipe=equipe)
    if db_equipe is None:
        raise HTTPException(status_code=404, detail="Équipe non trouvée")
    return db_equipe


@app.delete("/equipes/{equipe_id}")
def delete_equipe(equipe_id: int, db: Session = Depends(get_db)):
    db_equipe = crud.delete_equipe(db, equipe_id=equipe_id)
    if db_equipe is None:
        raise HTTPException(status_code=404, detail="Équipe non trouvée")
    return {"message": "Équipe supprimée avec succès"}


@app.post("/joueurs/", response_model=Joueur)
def create_joueur(joueur: JoueurCreate, db: Session = Depends(get_db)):
    if joueur.equipe_id:
        db_equipe = crud.get_equipe(db, equipe_id=joueur.equipe_id)
        if not db_equipe:
            raise HTTPException(status_code=404, detail="Équipe non trouvée")
    return crud.create_joueur(db=db, joueur=joueur)


@app.get("/joueurs/", response_model=List[Joueur])
def read_joueurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    joueurs = crud.get_joueurs(db, skip=skip, limit=limit)
    return joueurs


@app.get("/joueurs/{joueur_id}", response_model=Joueur)
def read_joueur(joueur_id: int, db: Session = Depends(get_db)):
    db_joueur = crud.get_joueur(db, joueur_id=joueur_id)
    if db_joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return db_joueur


@app.get("/equipes/{equipe_id}/joueurs/", response_model=List[Joueur])
def read_joueurs_by_equipe(equipe_id: int, db: Session = Depends(get_db)):
    db_equipe = crud.get_equipe(db, equipe_id=equipe_id)
    if not db_equipe:
        raise HTTPException(status_code=404, detail="Équipe non trouvée")
    return crud.get_joueurs_by_equipe(db, equipe_id=equipe_id)


@app.put("/joueurs/{joueur_id}", response_model=Joueur)
def update_joueur(joueur_id: int, joueur: JoueurUpdate, db: Session = Depends(get_db)):
    if joueur.equipe_id:
        db_equipe = crud.get_equipe(db, equipe_id=joueur.equipe_id)
        if not db_equipe:
            raise HTTPException(status_code=404, detail="Équipe non trouvée")
    
    db_joueur = crud.update_joueur(db, joueur_id=joueur_id, joueur=joueur)
    if db_joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return db_joueur


@app.delete("/joueurs/{joueur_id}")
def delete_joueur(joueur_id: int, db: Session = Depends(get_db)):
    db_joueur = crud.delete_joueur(db, joueur_id=joueur_id)
    if db_joueur is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    return {"message": "Joueur supprimé avec succès"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 