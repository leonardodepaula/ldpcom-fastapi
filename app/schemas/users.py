from typing import Optional
from pydantic import BaseModel, EmailStr

# User creation schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str