from fastapi import FastAPI
from app.routers import health
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.db.mongo import connect_to_mongo, close_mongo_connection
from contextlib import asynccontextmanager
from app.core.logger import setup_logger
from app.routers import influencer

setup_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()
    
app = FastAPI(
    title="Clone Social API",
    description="API oficial da plataforma Clone Social: automações com n8n, WhatsApp, Supabase, geração de conteúdo e mais.",
    version="1.0.0",
    docs_url="/docs",    # Swagger
    redoc_url="/redoc",   # ReDoc
    lifespan=lifespan 
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("static/favicon2.ico")

app.include_router(health.router)
app.include_router(influencer.router)