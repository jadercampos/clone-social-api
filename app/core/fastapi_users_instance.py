from fastapi_users import FastAPIUsers
from app.models.postgres.user import User
from app.core.security import auth_backend
from app.core.user_manager import get_user_manager
from uuid import UUID

fastapi_users = FastAPIUsers[User, UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
