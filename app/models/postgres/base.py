import uuid
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func
from app.db.base import Base

class BaseModelORM(Base):
    __abstract__ = True  # não cria tabela

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
