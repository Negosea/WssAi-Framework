import os
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuração simples
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/sea/WssAi-Framework/backend/wssai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo básico
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

# Criação do banco
with app.app_context():
    db.create_all()
    print("✅ Banco criado com sucesso!")
    print(f"Local: {app.config['SQLALCHEMY_DATABASE_URI']}")