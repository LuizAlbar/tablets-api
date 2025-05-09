from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost:3306/products"

    
settings = Setting()