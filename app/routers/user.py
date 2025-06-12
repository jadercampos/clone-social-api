from fastapi import APIRouter, Depends, HTTPException, status
from app.models.postgres.user import User
from app.core.fastapi_users_instance import current_active_user, current_superuser
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
async def get_me(user: User = Depends(current_active_user)):
    try:
        logger.info(f"[USERS/ME] Usuário autenticado: {user.email}")
        return {
            "status": "ok",
            "data": {
                "id": str(user.id),
                "email": user.email,
                "is_active": user.is_active,
                "is_verified": user.is_verified,
                "is_superuser": user.is_superuser,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            },
        }
    except Exception as e:
        logger.exception("[USERS/ME] Erro ao recuperar dados do usuário")
        raise HTTPException(status_code=500, detail="Erro interno ao buscar usuário")


@router.get("/admin-only")
async def admin_info(user: User = Depends(current_superuser)):
    try:
        logger.info(f"[ADMIN] Acesso autorizado para: {user.email}")
        return {
            "status": "ok",
            "message": f"Bem-vindo, admin {user.email}",
            "data": {
                "user_id": str(user.id),
                "superuser": user.is_superuser,
            },
        }
    except Exception as e:
        logger.exception("[ADMIN] Erro ao processar rota admin")
        raise HTTPException(status_code=500, detail="Erro interno para admin")
