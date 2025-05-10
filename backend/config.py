import os

class Config:
    TESSERACT_CMD = '/usr/bin/tesseract'
    POPPLER_PATH = '/usr/bin'
    UPLOAD_FOLDER = 'uploads/'


# backend/config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///wssai.db'
    UPLOAD_FOLDER = 'backend/uploads'

# app.py
app.config.from_object('config.Config') # type: ignore