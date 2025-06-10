from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

mongo_client: AsyncIOMotorClient = None

async def connect_to_mongo():
    global mongo_client
    mongo_client = AsyncIOMotorClient(settings.MONGO_URL)

async def close_mongo_connection():
    global mongo_client
    mongo_client.close()
