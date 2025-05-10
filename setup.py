# setup.py
from setuptools import setup, find_packages

setup(
    name="wssai",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        # outras dependências
    ],
)

# setup.py

setup(
    name="helena_core",
    version="0.1",
    package_dir={"": "backend/src"},
    packages=find_packages(where="backend/src"),
    install_requires=[
        "pdfplumber",
        "pytesseract",
        "pillow",
        "pdf2image"
    ],
)