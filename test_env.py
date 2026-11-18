from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    embedding_api_key: str = ""
    embedding_base_url: str = ""
    embedding_model: str = ""

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"   # 忽略.env里其他多余变量
    )

settings = Settings()
print("embedding_api_key =", repr(settings.embedding_api_key))
print("embedding_base_url =", repr(settings.embedding_base_url))
print("embedding_model =", repr(settings.embedding_model))
