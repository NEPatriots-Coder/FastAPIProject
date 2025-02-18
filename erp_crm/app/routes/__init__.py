from .auth import router as auth_router
from .customer import router as customer_router
from .contact import router as contact_router

__all__ = ['auth_router', 'customer_router', 'contact_router']
