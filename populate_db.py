from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, EquipeDB, JoueurDB
import crud
from models import EquipeCreate, JoueurCreate

Base.metadata.create_all(bind=engine)

def populate_database():
    db = SessionLocal()
    
    try:
        equipes_data = [
            {"nom": "Manchester City", "ville": "Manchester", "ligue": "Premier League"},
            {"nom": "Bayern Munich", "ville": "Munich", "ligue": "Bundesliga"},
            {"nom": "Paris Saint Germain", "ville": "Paris", "ligue": "Ligue 1"},
            {"nom": "FC Barcelona", "ville": "Barcelone", "ligue": "La Liga"},
        ]
        
        created_equipes = []
        for equipe_info in equipes_data:
            existing_equipe = db.query(EquipeDB).filter(
                EquipeDB.nom == equipe_info["nom"]
            ).first()
            
            if existing_equipe:
                print(f"Équipe déjà existante: {existing_equipe.nom}")
                created_equipes.append(existing_equipe)
            else:
                equipe_data = EquipeCreate(**equipe_info)
                equipe = crud.create_equipe(db, equipe_data)
                created_equipes.append(equipe)
                print(f"Équipe créée: {equipe.nom}")
        
        joueurs_data = [
            {"nom": "Debruyne", "prenom": "Kevin", "age": 34, "poste": "Milieu", "equipe_id": created_equipes[0].id},
            {"nom": "Cherki", "prenom": "Rayan", "age": 21, "poste": "Attaquant", "equipe_id": created_equipes[0].id},
            {"nom": "Olise", "prenom": "Michael", "age": 23, "poste": "Ailier", "equipe_id": created_equipes[1].id},
            {"nom": "Neuer", "prenom": "Manuel", "age": 39, "poste": "Gardien", "equipe_id": created_equipes[1].id},
            {"nom": "Hakimi", "prenom": "Achraf", "age": 26, "poste": "Defenseur", "equipe_id": created_equipes[2].id},
            {"nom": "Neymar", "prenom": "Jr", "age": 33, "poste": "Ailier", "equipe_id": created_equipes[3].id},
            {"nom": "Yamal", "prenom": "Lamine", "age": 18, "poste": "Ailier", "equipe_id": None},
        ]
        
        for joueur_info in joueurs_data:
            existing_joueur = db.query(JoueurDB).filter(
                JoueurDB.nom == joueur_info["nom"],
                JoueurDB.prenom == joueur_info["prenom"]
            ).first()
            
            if existing_joueur:
                equipe_nom = "Libre" if not existing_joueur.equipe_id else next((e.nom for e in created_equipes if e.id == existing_joueur.equipe_id), "Équipe inconnue")
                print(f"Joueur déjà existant: {existing_joueur.prenom} {existing_joueur.nom} ({equipe_nom})")
            else:
                joueur_data = JoueurCreate(**joueur_info)
                joueur = crud.create_joueur(db, joueur_data)
                equipe_nom = "Libre" if not joueur.equipe_id else next((e.nom for e in created_equipes if e.id == joueur.equipe_id), "Équipe inconnue")
                print(f"Joueur créé: {joueur.prenom} {joueur.nom} ({equipe_nom})")
        
        print("\nBase de données peuplée avec succès!")
        
    except Exception as e:
        print(f"Erreur lors du peuplement: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_database() 