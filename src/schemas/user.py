from pydantic import BaseModel
from pydantic import EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class ViewUser(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
