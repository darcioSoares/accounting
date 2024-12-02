from typing import Optional
from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    email: str  # Ajustado para String
    password: str  # Ajustado para String
    roles: str

    class Config:
        orm_mode = True


class UserSchema(UserCreateSchema):
    id: Optional[int]  # O ID será gerado pelo banco

