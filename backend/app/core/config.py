from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    REDIS_PORT: int

    DB_HOST: str = "localhost"

    class Config:
        env_file = ".env"


settings = Settings()


def get_database_url() -> str:
    return (
        f"postgresql+psycopg://{settings.DB_USER}:"
        f"{settings.DB_PASSWORD}@{settings.DB_HOST}:"
        f"{settings.DB_PORT}/{settings.DB_NAME}"
    )
