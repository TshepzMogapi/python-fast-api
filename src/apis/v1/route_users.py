from db.repository.user import create_new_user
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.user import CreateUser
from schemas.user import ViewUser
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ViewUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
