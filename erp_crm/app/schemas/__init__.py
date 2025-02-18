# app/schemas/__init__.py
from .user import UserBase, UserCreate, User
from .customer import CustomerBase, CustomerCreate, CustomerResponse
from .contact import ContactBase, ContactCreate, ContactResponse

__all__ = [
    'UserBase', 'UserCreate', 'User',
    'CustomerBase', 'CustomerCreate', 'CustomerResponse',
    'ContactBase', 'ContactCreate', 'ContactResponse'
]