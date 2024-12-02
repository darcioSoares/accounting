from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.schemas.user import UserCreateSchema, UserSchema
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()
#/api/v1/users

@router.get("/", response_model=list[UserSchema])
async def get_cursos(session: AsyncSession = Depends(get_session)):
    return await user_service.get_all(session)

@router.get("/{curso_id}", response_model=UserSchema)
async def get_curso(curso_id: int, session: AsyncSession = Depends(get_session)):
    curso = await user_service.get_by_id(session, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.post("/", response_model=UserSchema)
async def create_curso(curso: UserCreateSchema, session: AsyncSession = Depends(get_session)):
    return await user_service.create(session, curso)

@router.put("/{curso_id}", response_model=UserSchema)
async def update_curso(curso_id: int, curso: UserSchema, session: AsyncSession = Depends(get_session)):
    updated = await user_service.update(session, curso_id, curso)
    if not updated:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return updated

@router.delete("/{curso_id}")
async def delete_curso(curso_id: int, session: AsyncSession = Depends(get_session)):
    deleted = await user_service.delete(session, curso_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return {"detail": "Curso deletado com sucesso"}
