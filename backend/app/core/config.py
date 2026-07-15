from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "ERIS"

    ENV: str = "development"

    DATABASE_URL: str = "sqlite:///eris.db"

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
