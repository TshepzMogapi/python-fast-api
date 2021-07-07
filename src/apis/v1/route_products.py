from apis.v1.route_users import create_user
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.product import Product
from schemas.product import CreateProduct, ViewProduct
from db.repository.product import create_new_product, get_product_by_id

router = APIRouter()

@router.post("/create",response_model=ViewProduct)
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
  create_user = 1
  product = create_new_product(product=product,db=db, owner_id=create_user)
  return product

@router.get("/{id}", response_model=ViewProduct)
def get_product(id: int, db: Session = Depends(get_db)):
  product = get_product_by_id(id=id,db=db)
  if not product:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product with id {id} does not exist")
  return product


