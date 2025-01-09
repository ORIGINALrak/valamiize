from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    CORS_ORIGINS: list[AnyHttpUrl] = [
        
    ]

    class Config:
        env_file = './.env'


settings = Settings()