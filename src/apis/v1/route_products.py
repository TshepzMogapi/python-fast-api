from db.repository.product import create_new_product
from db.repository.product import get_product_by_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.product import CreateProduct
from schemas.product import ViewProduct
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create", response_model=ViewProduct)
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    create_user = 1
    product = create_new_product(product=product, db=db, owner_id=create_user)
    return product


@router.get("/{id}", response_model=ViewProduct)
def get_product(id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(id=id, db=db)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} does not exist",
        )
    return product
