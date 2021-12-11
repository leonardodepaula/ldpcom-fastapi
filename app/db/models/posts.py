#SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Project
from db.base_class import Base

class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,nullable= False)
    content = Column(String, nullable=False)
    author_id =  Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='posts')