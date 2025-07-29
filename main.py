from fastapi import FastAPI

app = FastAPI(
    title="Orchestrateur Football",
    description="API de gestion des joueurs et équipes de football",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'orchestrateur de football"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 