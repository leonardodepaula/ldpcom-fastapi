# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker

# Project
from core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)