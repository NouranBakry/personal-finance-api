from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # These names must match the keys in your .env exactly
    DATABASE_URL: str
    SECRET_KEY: str
    ENVIRONMENT: str
    # This line tells Pydantic to look for a file named ".env"
    # in the root of your project
    model_config = SettingsConfigDict(env_file=".env")


# Create a single instance to be used across the app
settings = Settings()
