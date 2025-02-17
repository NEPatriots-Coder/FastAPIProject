from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, customers, contacts
from .database import engine
from .models import user, customer, contact

# Create database tables
user.Base.metadata.create_all(bind=engine)
customer.Base.metadata.create_all(bind=engine)
contact.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ERP/CRM System",
    description="A simple ERP/CRM system with basic functionality",
    version="0.1.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(customers.router, prefix="/api/customers", tags=["Customers"])
app.include_router(contacts.router, prefix="/api/contacts", tags=["Contacts"])