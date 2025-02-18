# setup.py
from setuptools import setup, find_packages

setup(
    name="erp_crm",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "sqlalchemy>=1.4.23",
        "pydantic>=1.8.2",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.5",
        "pytest>=7.4.0",
        "httpx>=0.24.1",
    ],
)