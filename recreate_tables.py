import asyncio
from app.core.database import engine, Base
from sqlalchemy.ext.asyncio import AsyncEngine

async def recreate_tables():
    if not isinstance(engine, AsyncEngine):
        raise TypeError("O engine não está configurado como AsyncEngine.")

    async with engine.begin() as conn:
        print("Apagando tabelas...")
        await conn.run_sync(Base.metadata.drop_all)
        print("Tabelas apagadas com sucesso.")

        print("Criando tabelas...")
        await conn.run_sync(Base.metadata.create_all)
        print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    asyncio.run(recreate_tables())
