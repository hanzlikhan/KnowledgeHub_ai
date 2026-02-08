from fastapi import FastAPI
from app.core.config import settings
from app.utils.logger import logger

app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def health():
    logger.info("Health check called")
    return {"status": "ok", "app": settings.APP_NAME}
