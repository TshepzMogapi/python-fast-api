from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
  email: EmailStr
  password: str

class ViewUser(BaseModel):
  email: EmailStr
  is_active: bool

  class Config():
    orm_mode = True
  