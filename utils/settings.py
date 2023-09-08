import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    print(f"database : {os.environ.get('MONGO_URL')}")
    ENV:str = "dev"
    MONGO_URL:str = os.environ.get('MONGO_URL')
