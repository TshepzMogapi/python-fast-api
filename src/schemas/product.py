from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date_created: Optional[date] = datetime.now().date()


class CreateProduct(ProductBase):
    title: str
    description: str


class ViewProduct(ProductBase):
    title: str
    description: str
    date_created: date

    class Config:
        orm_mode = True
