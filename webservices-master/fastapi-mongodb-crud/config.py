from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    MONGO_PORT: int
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DB: str
    MONGO_HOSTNAME: str

    CORS_ORIGINS: list[AnyHttpUrl] = [
        
    ]

    class Config:
        env_file = './.env'


settings = Settings()