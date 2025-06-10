from sqlalchemy import Column, String
from app.models.postgres.base import BaseModelORM

class Influencer(BaseModelORM):
    __tablename__ = "influencers"

    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
