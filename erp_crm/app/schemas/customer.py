# app/schemas/customer.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CustomerBase(BaseModel):
    company_name: str
    industry: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Updated from orm_mode = True
