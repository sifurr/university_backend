from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Central configuration class.
    Leads values from environment variables
    """

    PROJECT_NAME: str
    DATABASE_URL: str

    SECRECT_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYs: int

    class Config:

        env_file = ".env"


# Singleton settings instance
@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()