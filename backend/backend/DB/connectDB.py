from motor.motor_asyncio import AsyncIOMotorClient
import os
from beanie import init_beanie
from backend.constants import DB_NAME 
from backend.models import DOCUMENT_MODELS


async def connectDB():
  try:
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    database = client[DB_NAME]
    await init_beanie(database=database, document_models=DOCUMENT_MODELS)
    print(f"database connection successful {client.address}")
  except Exception as e:
    print(f"failed to connect to the database. {e}")