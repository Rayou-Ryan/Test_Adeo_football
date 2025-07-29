# Phase 6 - Production avec Docker

## Description

Version finale avec Docker, prête pour la production. Inclut l'orchestration complète et les scripts utilitaires.

## Fonctionnalités

- Application FastAPI complète
- CRUD équipes et joueurs
- Système de transferts
- Dockerisation avec PostgreSQL
- Scripts de gestion des données

## Lancement avec Docker

```bash
docker-compose up --build
```

## Scripts utilitaires

### Peupler la base de données
```bash
python populate_db.py
```

### Vider la base de données
```bash
python clear_db.py
```

## Services

- **App** : Application FastAPI sur le port 8000
- **DB** : PostgreSQL sur le port 5432

## Endpoints

### Équipes
- `POST /equipes/` - Créer une équipe
- `GET /equipes/` - Lister les équipes
- `GET /equipes/{id}` - Récupérer une équipe
- `PUT /equipes/{id}` - Modifier une équipe
- `DELETE /equipes/{id}` - Supprimer une équipe

### Joueurs
- `POST /joueurs/` - Créer un joueur
- `GET /joueurs/` - Lister les joueurs
- `GET /joueurs/{id}` - Récupérer un joueur
- `GET /equipes/{id}/joueurs/` - Joueurs d'une équipe
- `PUT /joueurs/{id}` - Modifier un joueur
- `DELETE /joueurs/{id}` - Supprimer un joueur

### Transferts
- `POST /joueurs/transfer` - Transférer un joueur

## Documentation API

- Swagger UI : `http://localhost:8000/docs`
- ReDoc : `http://localhost:8000/redoc`

## Commit suggéré (Conventional Commits)

```bash
git commit -m "build: add Docker support and production setup

- Add Dockerfile for application containerization
- Configure docker-compose with PostgreSQL service
- Add database population script
- Add database clearing utility
- Configure production-ready environment"
``` 