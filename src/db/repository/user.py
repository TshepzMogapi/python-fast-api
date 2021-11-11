from core.hashing import Hasher
from db.models.user import User
from schemas.user import CreateUser
from sqlalchemy.orm import Session


def create_new_user(user: CreateUser, db: Session):
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=False,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
