from uuid import UUID
from fastapi_users.manager import BaseUserManager
from fastapi_users.exceptions import UserAlreadyExists  # ✅ CORRETO
from app.models.postgres.user import User
from app.core.config import settings

class UserManager(BaseUserManager[User, UUID]):
    reset_password_token_secret = settings.RESET_PASSWORD_SECRET
    verification_token_secret = settings.EMAIL_VERIFICATION_SECRET

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
        print(f"✅ Usuário registrado: {user.email}")

    async def on_after_forgot_password(self, user: User, token: str, request=None):
        print(f"🔐 [RESET] {user.email} - Token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request=None):
        print(f"📩 [VERIFY] {user.email} - Token: {token}")
