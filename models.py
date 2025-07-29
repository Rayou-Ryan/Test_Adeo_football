from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EquipeBase(BaseModel):
    nom: str
    ville: str
    ligue: Optional[str] = None


class EquipeCreate(EquipeBase):
    pass


class EquipeUpdate(BaseModel):
    nom: Optional[str] = None
    ville: Optional[str] = None
    ligue: Optional[str] = None


class Equipe(EquipeBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class JoueurBase(BaseModel):
    nom: str
    prenom: str
    age: int
    poste: str
    equipe_id: Optional[int] = None


class JoueurCreate(JoueurBase):
    pass


class JoueurUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    age: Optional[int] = None
    poste: Optional[str] = None
    equipe_id: Optional[int] = None


class Joueur(JoueurBase):
    id: int
    created_at: datetime
    equipe: Optional[Equipe] = None
    
    class Config:
        from_attributes = True


class JoueurTransfer(BaseModel):
    joueur_id: int
    nouvelle_equipe_id: int 