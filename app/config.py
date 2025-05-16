from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    max_tokens: int = 1024
    secret_key: str = "change-me"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
