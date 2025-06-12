from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from uuid import UUID

from app.models.postgres.user import User
from app.schemas.postgres.user import UserRead, UserCreate, UserUpdate
from app.core.security import auth_backend
from app.db.postgres import get_db
from app.core.fastapi_users_instance import (
    fastapi_users,
    current_user,
    current_active_user,
    current_superuser,
)
from app.core.user_manager import get_user_db, UserManager

import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Auth"])

class LoginInput(BaseModel):
    email: str
    password: str

# 🔐 Rotas padrão do FastAPI Users
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Users"],
)

@router.post("/simple-login")
async def simple_login(
    data: LoginInput,
    db: AsyncSession = Depends(get_db),
):
    user_db_gen = get_user_db(db)
    user_db = await anext(user_db_gen)

    manager = UserManager(user_db)
    user = await user_db.get_by_email(data.email)

    if not user:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    valid, _ = manager.password_helper.verify_and_update(data.password, user.hashed_password)
    if not valid:
        raise HTTPException(status_code=401, detail="Senha inválida")

    strategy = auth_backend.get_strategy()
    access_token = await strategy.write_token(user)

    return JSONResponse(
        content={"access_token": access_token, "token_type": "bearer"}
    )
