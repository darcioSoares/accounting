from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import UserModel

class UserRepository:
    async def get_all(self, session: AsyncSession):
        query = select(UserModel)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, session: AsyncSession, curso_id: int):
        return await session.get(UserModel, curso_id)

    async def create(self, session: AsyncSession, curso: UserModel):
        session.add(curso)
        await session.commit()
        await session.refresh(curso)
        return curso

    async def update(self, session: AsyncSession, curso_id: int, updates: dict):
        curso = await self.get_by_id(session, curso_id)
        if curso:
            for key, value in updates.items():
                setattr(curso, key, value)
            await session.commit()
            await session.refresh(curso)
        return curso

    async def delete(self, session: AsyncSession, curso_id: int):
        curso = await self.get_by_id(session, curso_id)
        if curso:
            await session.delete(curso)
            await session.commit()
        return curso

