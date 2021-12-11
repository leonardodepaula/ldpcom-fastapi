# FastAPI
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Project
from core.config import settings
from db.session import engine
from db.base import Base

# Routers
from routers import home

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(home.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
Base.metadata.create_all(bind=engine)