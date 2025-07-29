from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from config import settings

SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class EquipeDB(Base):
    __tablename__ = "equipes"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, index=True)
    ville = Column(String)
    ligue = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    joueurs = relationship("JoueurDB", back_populates="equipe")


class JoueurDB(Base):
    __tablename__ = "joueurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String)
    age = Column(Integer)
    poste = Column(String)
    equipe_id = Column(Integer, ForeignKey("equipes.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    equipe = relationship("EquipeDB", back_populates="joueurs")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 