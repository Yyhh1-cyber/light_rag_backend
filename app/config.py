from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    llm_api_key: str = ""
    llm_base_url: str = ""
    llm_model: str = ""

    embedding_api_key: str = ""
    embedding_base_url: str = ""
    embedding_model: str = ""

    api_token: str = ""
    chroma_persist_path: str = "./chroma_db"
    upload_dir: str = "./uploads"
    max_file_size: int = 10485760
    allow_suffix: str = ".txt,.pdf"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
