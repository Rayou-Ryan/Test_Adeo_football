from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, EquipeDB, JoueurDB

Base.metadata.create_all(bind=engine)

def populate_database():
    db = SessionLocal()
    
    try:
        equipe1 = EquipeDB(nom="Paris Saint-Germain", ville="Paris", ligue="Ligue 1")
        equipe2 = EquipeDB(nom="Olympique de Marseille", ville="Marseille", ligue="Ligue 1")
        equipe3 = EquipeDB(nom="AS Monaco", ville="Monaco", ligue="Ligue 1")
        
        db.add_all([equipe1, equipe2, equipe3])
        db.commit()
        db.refresh(equipe1)
        db.refresh(equipe2)
        db.refresh(equipe3)
        
        joueur1 = JoueurDB(nom="Mbappé", prenom="Kylian", age=25, poste="Attaquant", equipe_id=equipe1.id)
        joueur2 = JoueurDB(nom="Neymar", prenom="Jr", age=32, poste="Ailier", equipe_id=equipe1.id)
        joueur3 = JoueurDB(nom="Payet", prenom="Dimitri", age=37, poste="Milieu", equipe_id=equipe2.id)
        joueur4 = JoueurDB(nom="Ben Yedder", prenom="Wissam", age=34, poste="Attaquant", equipe_id=equipe3.id)
        
        db.add_all([joueur1, joueur2, joueur3, joueur4])
        db.commit()
        
        print("Base de données peuplée avec succès!")
        
    except Exception as e:
        print(f"Erreur lors du peuplement: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_database() 