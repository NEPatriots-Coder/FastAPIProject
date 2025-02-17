from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.database import engine, Base
from routes.auth import router as auth_router
from routes.customer import router as customer_router
from routes.contact import router as contact_router


# Create database tables
Base.metadata.create_all(bind=engine)

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
app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(contact_router)

@app.get("/")
def read_root():
    return {"Hello: ERP_CRM"}