import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV:str = "dev"
    MONGO_URL:str = "mongodb://db:27017/test" #os.environ.get('MONGO_URL')
