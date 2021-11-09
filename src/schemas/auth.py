from pydantic import BaseModel
from pydantic import EmailStr


class UserEmailPasswordAuth(BaseModel):
    email: EmailStr
    password: str
