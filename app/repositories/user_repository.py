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

    #paginação
    # from sqlalchemy import func

    # async def get_all(self, session: AsyncSession, page: int = 1, page_size: int = 10):
    #     # Calcula o ponto de partida para a consulta
    #     offset = (page - 1) * page_size

    #     # Consulta o total de registros
    #     total_query = select(func.count(UserModel.id))
    #     total = await session.execute(total_query)
    #     total_count = total.scalar()

    #     # Constrói a query com paginação
    #     query = select(UserModel).limit(page_size).offset(offset)
    #     result = await session.execute(query)
    #     records = result.scalars().all()

    #     # Calcula o total de páginas
    #     total_pages = (total_count + page_size - 1) // page_size

    #     # Retorna os registros e informações de paginação
    #     return {
    #         "records": records,
    #         "total": total_count,
    #         "page": page,
    #         "page_size": page_size,
    #         "total_pages": total_pages,
    #     }

#     Explicação
# Parâmetros page e page_size:

# page: A página atual (começa em 1).
# page_size: O número de registros por página.
# Cálculo do Offset:

# O offset é calculado como (page - 1) * page_size. Por exemplo:
# Se page=1 e page_size=10, o offset será 0.
# Se page=2 e page_size=10, o offset será 10.
# Métodos limit e offset:

# limit: Restringe o número de registros retornados.
# offset: Pula os primeiros n registros antes de começar a retornar os resultados.