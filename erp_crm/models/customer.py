from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base

class Customer(Base):
    __tablename__="custmers"


    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    industry = Column(String)
    address = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())