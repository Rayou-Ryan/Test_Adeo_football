import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://orchestrator:password123@db:5432/orchestrator_db"
    postgres_user: str = "orchestrator"
    postgres_password: str = "password123"
    postgres_db: str = "orchestrator_db"
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings() 