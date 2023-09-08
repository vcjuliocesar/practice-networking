from pymongo.mongo_client import MongoClient
from utils.settings import Settings

settings = Settings()

uri = settings.MONGO_URL

client = MongoClient(uri)

db = client["test-database"]


