from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool = False

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SECRET_KEY: str

    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
