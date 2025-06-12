from sqlalchemy.orm import Mapped, mapped_column
from app.models.postgres.base import BaseModelORM

class Influencer(BaseModelORM):
    __tablename__ = "influencers"

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str | None] = mapped_column(nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(nullable=True)
