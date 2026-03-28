from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    app_name: str = "Recipe Box Service"
    default_page_size: int = 20
    feature_preview: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",           # Load from .env file
        env_prefix="RECIPE_",      # Only read RECIPE_* variables
        extra="ignore",            # Ignore unknown variables
    )