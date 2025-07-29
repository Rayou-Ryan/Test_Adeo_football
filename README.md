# Phase 1 - Base FastAPI

## Description

Cette phase établit la structure de base de l'application FastAPI avec une configuration minimale.

## Fonctionnalités

- Application FastAPI de base
- Configuration avec pydantic-settings
- Endpoint racine fonctionnel
- Structure de projet propre

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python main.py
```

L'application sera disponible sur `http://localhost:8000`

## Endpoints

- `GET /` - Message de bienvenue

## Commit suggéré (Conventional Commits)

```bash
git commit -m "feat: initialize FastAPI application with basic structure

- Add FastAPI application setup
- Configure pydantic settings
- Add root endpoint for health check
- Set up project structure and requirements"
``` 