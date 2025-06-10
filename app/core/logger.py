import logging
from logging.config import dictConfig
from app.core.config import settings

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # importante para FastAPI/uvicorn
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
        },
        "colored": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
            "log_colors": {
                "DEBUG": "white",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "EXCEPTION": "pink",
                "CRITICAL": "bold_red",
            },
        },
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "colored",  # mude para "default" se quiser sem cor
        },
    },
    "root": {
        "level": settings.LOG_LEVEL or "INFO",
        "handlers": ["default"],
    },
    "loggers": {
        "uvicorn": {"level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"level": "WARNING"},
        "pymongo": {"level": "WARNING"},
    },
}

def setup_logger():
    dictConfig(LOG_CONFIG)
    logging.getLogger(__name__).info("Logger configurado com sucesso!")
