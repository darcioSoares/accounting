from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from datetime import datetime

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)  # Alterado para String
    password = Column(String(255), nullable=False)  # Alterado para String
    roles = Column(String(50), nullable=True)  # Alterado para String
    created_at = Column(DateTime, default=datetime.now, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
