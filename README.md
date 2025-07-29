# Orchestrateur Football

API de gestion des joueurs et équipes de football développée avec FastAPI et PostgreSQL.

## Fonctionnalités

- Gestion des équipes (CRUD)
- Gestion des joueurs (CRUD)
- Transfert de joueurs entre équipes
- Base de données PostgreSQL
- Interface Swagger automatique
- Conteneurisation Docker

## Prérequis

- Docker et Docker Compose
- Python 3.8+ (pour développement local)

## Installation et démarrage

### Avec Docker (recommandé)

1. Cloner le projet :
```bash
git clone <url-du-repo>
cd orchestrator
```

2. Démarrer l'application :
```bash
docker-compose up --build
```

3. L'API sera accessible à l'adresse : http://localhost:8000

4. Interface Swagger : http://localhost:8000/docs

### Développement local

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Configurer la base de données PostgreSQL
3. Démarrer l'application :
```bash
uvicorn main:app --reload
```

## Endpoints disponibles

### Équipes

- `POST /equipes/` - Créer une équipe
- `GET /equipes/` - Lister toutes les équipes
- `GET /equipes/{equipe_id}` - Obtenir une équipe spécifique
- `PUT /equipes/{equipe_id}` - Modifier une équipe
- `DELETE /equipes/{equipe_id}` - Supprimer une équipe
- `GET /equipes/{equipe_id}/joueurs/` - Lister les joueurs d'une équipe

### Joueurs

- `POST /joueurs/` - Créer un joueur
- `GET /joueurs/` - Lister tous les joueurs
- `GET /joueurs/{joueur_id}` - Obtenir un joueur spécifique
- `PUT /joueurs/{joueur_id}` - Modifier un joueur
- `DELETE /joueurs/{joueur_id}` - Supprimer un joueur
- `POST /joueurs/transfer` - Transférer un joueur vers une autre équipe

## Exemples d'utilisation

### Créer une équipe
```bash
curl -X POST "http://localhost:8000/equipes/" \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Manchester City",
    "ville": "Manchester",
    "ligue": "Premiere league"
  }'
```

### Créer un joueur
```bash
curl -X POST "http://localhost:8000/joueurs/" \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Debruyne",
    "prenom": "Kevin",
    "age": 34,
    "poste": "Milieu",
    "equipe_id": 1
  }'
```

### Transférer un joueur
```bash
curl -X POST "http://localhost:8000/joueurs/transfer" \
  -H "Content-Type: application/json" \
  -d '{
    "joueur_id": 1,
    "nouvelle_equipe_id": 2
  }'
```

## Structure du projet

```
orchestrator/
├── main.py              # Application FastAPI principale
├── models.py            # Modèles Pydantic
├── database.py          # Configuration base de données
├── crud.py              # Opérations CRUD
├── config.py            # Configuration de l'application
├── requirements.txt     # Dépendances Python
├── Dockerfile           # Configuration Docker
├── docker-compose.yml   # Orchestration des services
└── README.md           # Documentation
```

## Configuration

Les variables d'environnement peuvent être configurées dans le fichier `config.py` :

- `DATABASE_URL` : URL de connexion PostgreSQL
- `HOST` : Adresse d'écoute de l'API
- `PORT` : Port d'écoute de l'API

## Base de données

La base de données PostgreSQL est automatiquement initialisée au démarrage avec les tables nécessaires :

- `equipes` : Stockage des équipes
- `joueurs` : Stockage des joueurs avec référence à l'équipe

## Technologies utilisées

- **FastAPI** : Framework web moderne et rapide
- **PostgreSQL** : Base de données relationnelle
- **SQLAlchemy** : ORM Python
- **Pydantic** : Validation et sérialisation des données
- **Uvicorn** : Serveur ASGI
- **Docker** : Conteneurisation
