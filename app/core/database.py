from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import AsyncGenerator
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not all([DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME]):
    raise ValueError("Uma ou mais variáveis de ambiente estão ausentes.")


print(f"Conectando ao banco de dados {DATABASE_NAME} com usuário {DATABASE_USER}.")


#DATABASE_URL = "postgresql+asyncpg://postgres:soares@localhost:5432/picoles"
DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_async_engine(DATABASE_URL, echo=False) #echo ref aos logs do sqlalchemy
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        print("Sessão aberta")
        yield session
        print("Sessão encerrada")

