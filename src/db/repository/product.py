from sqlalchemy.orm import Session

from schemas.product import CreateProduct
from db.models.product import Product

def create_new_product(product: CreateProduct, db: Session, owner_id: int):
  product_object = Product(**product.dict(), owner_id=owner_id,)
  db.add(product_object)
  db.commit()
  db.refresh(product_object)
  return product_object

def get_product_by_id(id: int, db: Session):
  product = db.query(Product).filter(Product.id == id).first()
  return product