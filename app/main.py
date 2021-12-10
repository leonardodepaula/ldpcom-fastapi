# FastAPI
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings

# Routers
from routers import home

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(home.router)
app.mount("/static", StaticFiles(directory="static"), name="static")