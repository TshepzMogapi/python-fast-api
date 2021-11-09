from datetime import timedelta

from apis.v1.route_users import create_user
from core.config import settings
from core.hashing import Hasher
from core.security import create_token
from db.repository.auth import get_user_by_email
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.auth import UserEmailPasswordAuth
from schemas.token import Token
from schemas.user import CreateUser
from schemas.user import ViewUser
from sqlalchemy.orm import Session

router = APIRouter()


def authenticate_email_password(email: str, password: str, db: Session):
    user = get_user_by_email(email=email, db=db)
    if not user:
        return False

    if not Hasher.verify_password(password, user.password):
        return False

    return user


@router.post("/sign-up-email", response_model=ViewUser)
def sign_up_with_email_and_password(user: CreateUser, db: Session = Depends(get_db)):
    user = create_user(user, db=db)
    return user


@router.post("/sign-in-email", response_model=Token)
def sign_in_with_email_and_password(
    auth_data: UserEmailPasswordAuth, db: Session = Depends(get_db)
):
    user = authenticate_email_password(auth_data.email, auth_data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token_expires = timedelta(minutes=int(settings.TOKEN_EXPIRE_MINUTES))
    token = create_token(data={"sub": auth_data.email}, expires_delta=token_expires)
    return {"token": token, "type": "bearer"}
