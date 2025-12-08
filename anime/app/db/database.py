import os
from motor.motor_asyncio import AsyncIOMotorClient
# "mongodb://localhost:27017/mydatabase"                                        
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/anime")
client = AsyncIOMotorClient(MONGO_URI)
db = client.get_default_database()