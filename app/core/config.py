from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Project info
    PROJECT_NAME: str = "Public Data Pipeline"

    # Infrastructure (safe defaults)
    KAFKA_BROKER_URL: str = "localhost:9092"
    KAFKA_TOPIC_RAW: str = "web_data_raw"
    POSTGRES_URL: str = "postgresql+asyncpg://user:pass@localhost/pipeline_db"

    # Pipeline settings
    PIPELINE_BATCH_SIZE: int = 100
    LOG_LEVEL: str = "INFO"

    # Optional API key for future sources (not used for public sources)
    DATA_SOURCE_API_KEY: str | None = None

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
