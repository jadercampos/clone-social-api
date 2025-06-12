from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from fastapi.security import HTTPBearer
from app.core.logger import setup_logger
from app.db.mongo import connect_to_mongo, close_mongo_connection
from app.routers import health, influencer, auth, user


setup_logger()

security = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()

app = FastAPI(
    title="Clone Social API",
    description="API oficial da plataforma Clone Social: automações com n8n, WhatsApp, Supabase, geração de conteúdo e mais.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# 🔐 Configura o botão "Authorize" do Swagger para usar token JWT
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    # Aplica o esquema como default em todas as rotas
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# 📁 Static files e favicon
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("static/favicon2.ico")

# 🚀 Rotas
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(influencer.router)
