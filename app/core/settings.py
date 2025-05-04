from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    
    DATABASE_URL : str = 'sqlite:///./store.db'
    
    class Config:
        env_file = '.env'
        
settings = Setting()