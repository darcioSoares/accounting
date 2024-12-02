from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserSchema
from app.models.user import UserModel
from app.repositories.user_repository import UserRepository

from app.core.redis import redis_client as redis
import logging

user_repository = UserRepository()

class UserService:
    async def get_all(self, session: AsyncSession):  
        nome: str = "Darcio"
        logging.info(f"Rota principal acessadadarcioooooo. {nome}")
        return await user_repository.get_all(session)

    async def get_by_id(self, session: AsyncSession, user_id: int):
        return await user_repository.get_by_id(session, user_id)

    async def create(self, session: AsyncSession, user: UserSchema):   
        novo_user = UserModel(**user.dict(exclude_unset=True))
        return await user_repository.create(session, novo_user)

    async def update(self, session: AsyncSession, user_id: int, user: UserSchema):
        updates = user.dict(exclude_unset=True)
        return await user_repository.update(session, user_id, updates)

    async def delete(self, session: AsyncSession, user_id: int):
        return await user_repository.delete(session, user_id)
