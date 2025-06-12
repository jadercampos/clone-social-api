from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Ambiente
    ENVIRONMENT: str = "dev"
    LOG_LEVEL: str = "INFO"
    
    # Segurança
    JWT_SECRET: str
    RESET_PASSWORD_SECRET: str
    EMAIL_VERIFICATION_SECRET: str
    
    # Banco de dados Postgres
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Banco de dados Mongo
    MONGO_URL: str = "mongodb://localhost:27017"
    
    @property
    def POSTGRES_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
