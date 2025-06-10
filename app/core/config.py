from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Config do banco principal
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    LOG_LEVEL: str = "DEBUG"

    # Config do Mongo (opcional)
    MONGO_URL: str = "mongodb://localhost:27017"

    # Ambiente
    ENVIRONMENT: str = "dev"

    @property
    def POSTGRES_URL(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
