# backend/src/auth/routes.py
from flask import Blueprint # type: ignore

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    pass