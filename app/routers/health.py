from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from sqlalchemy import text
from app.db import mongo
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
async def health_check():
    return {"status": "API is alive!!!"}

@router.get("/postgres")
def db_healthcheck(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        logger.error("Error checking postgres")
        return {"status": "error", "detail": str(e)}

@router.get("/mongo")
async def check_mongo():
    if mongo.mongo_client is None:
        logger.error("Mongo client not initialized")
        return {"status": "error", "detail": "Mongo client not initialized"}
    try:
        await mongo.mongo_client.admin.command("ping")
        return {"status": "ok"}
    except Exception as e:
        logger.error("Error checking mongo")
        return {"status": "error", "detail": str(e)}

@router.get("/logger")
async def check_logger():
    logger.debug("Isso é um debug.")
    logger.info("Isso é um info.")
    logger.warning("Isso é um aviso.")
    logger.error("Isso é um erro.")
    logger.critical("Isso é crítico!")
    # logger.exception("Isso é uma exceção.")
    
    return {"status": "ok"}
