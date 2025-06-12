from uuid import UUID
from fastapi_users.manager import BaseUserManager
from fastapi_users.exceptions import UserAlreadyExists
from app.models.postgres.user import User
from app.core.config import settings
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from fastapi import Depends
from app.db.postgres import get_db

class UserManager(BaseUserManager[User, UUID]):
    user_db_model = User
    reset_password_token_secret = settings.RESET_PASSWORD_SECRET
    verification_token_secret = settings.EMAIL_VERIFICATION_SECRET
    
    def parse_id(self, user_id: str) -> UUID:
        return UUID(user_id)
    
    async def create(
        self,
        user_create,
        safe: bool = False,
        request=None,
    ) -> User:
        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user:
            raise UserAlreadyExists()
        return await super().create(user_create, safe, request)

    async def on_after_register(self, user: User, request=None):
        print(f"[REGISTER] Novo usuário registrado: {user.email}")

    async def on_after_forgot_password(self, user: User, token: str, request=None):
        print(f"[FORGOT] {user.email} solicitou reset de senha. Token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request=None):
        print(f"[VERIFY] {user.email} solicitou verificação. Token: {token}")

async def get_user_db(session: AsyncSession = Depends(get_db)) -> AsyncGenerator:
    yield SQLAlchemyUserDatabase(session, User)

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)

