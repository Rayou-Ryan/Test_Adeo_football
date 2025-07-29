from database import SessionLocal, Base, engine

def clear_database():
    db = SessionLocal()
    
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        print("Base de données vidée et recréée avec succès!")
        
    except Exception as e:
        print(f"Erreur lors du vidage: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    clear_database() 