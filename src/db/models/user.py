from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, nullable=False, unique=True,index=True)
  password = Column(String, nullable=False)
  is_active = Column(Boolean(), default=False)
  is_superuser = Column(Boolean(), default=False)
  products = relationship("Product", back_populates="owner")