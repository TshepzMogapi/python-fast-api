from apis.v1.route_users import create_user
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.user import CreateUser
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/sign-up-email")
def sign_up_with_email_and_password(user: CreateUser, db: Session = Depends(get_db)):
    user = create_user(user, db=db)
    return user
