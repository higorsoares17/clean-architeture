from configs.database import engine
import configs.environment as dbmodel
from repositories.user_repository import UserRepository
from configs.security import generate_hash
from models.user_model import UserModel


async def create_tables() -> None:
    import models.__all_models
    async with engine.begin() as conn:
        await conn.run_sync(dbmodel.DB_BASE_MODEL.metadata.create_all)
        await UserRepository().create_user(UserModel(
            email="sesatech@sesa.com", password=generate_hash("sesatech")
        ))

def init():
    import asyncio
    asyncio.run(create_tables())


init()