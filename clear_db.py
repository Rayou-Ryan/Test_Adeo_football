from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, EquipeDB, JoueurDB

def clear_database():
    db = SessionLocal()
    
    try:
        print("Suppression de tous les joueurs...")
        joueurs_count = db.query(JoueurDB).count()
        db.query(JoueurDB).delete()
        print(f"{joueurs_count} joueurs supprimés")
        
        print("Suppression de toutes les équipes...")
        equipes_count = db.query(EquipeDB).count()
        db.query(EquipeDB).delete()
        print(f"{equipes_count} équipes supprimées")
        
        db.commit()
        print("\nBase de données vidée avec succès!")
        
    except Exception as e:
        print(f"Erreur lors du vidage: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    confirmation = input("Êtes-vous sûr de vouloir vider la base de données ? (oui/non): ")
    if confirmation.lower() in ['oui', 'o', 'yes', 'y']:
        clear_database()
    else:
        print("Opération annulée.") 