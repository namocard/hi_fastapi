from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DATABASE_URI: PostgresDsn = "postgres://user:pass@localhost:5432/foobar"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
