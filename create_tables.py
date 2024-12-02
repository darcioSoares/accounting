import asyncio
from app.core.database import engine, Base
import app.models.user

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    asyncio.run(create_tables())
