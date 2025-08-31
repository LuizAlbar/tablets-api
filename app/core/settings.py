from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    
    DATABASE_URL: str = "sqlite:///./store.db"
    
settings = Setting()
