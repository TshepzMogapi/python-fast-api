from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Product(Base):
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  description = Column(String, nullable=False)
  date_created = Column(Date)
  is_active = Column(Boolean(), default=True)
  owner_id = Column(Integer, ForeignKey("user.id"))
  owner = relationship("User", back_populates ="products")

  

