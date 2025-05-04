from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    
    database_url : str = 'sqlite:///./store.db'
    
    class Config:
        env_file = '.env'
        
settings = Setting()