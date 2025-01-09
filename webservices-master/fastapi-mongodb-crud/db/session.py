from beanie import init_beanie
import motor.motor_asyncio

from config import settings
from db.models import Check, Procedure


DATABASE_URL = 'mongodb://' \
                f'{settings.MONGO_USER}:' \
                f'{settings.MONGO_PASSWORD}@' \
                f'{settings.MONGO_HOSTNAME}:' \
                f'{settings.MONGO_PORT}/' \
                f'{settings.MONGO_DB}' \
                '?authSource=admin'


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        DATABASE_URL,
        uuidRepresentation="standard"
    )

    await init_beanie(database=client.get_default_database(), document_models=[Check, Procedure])
