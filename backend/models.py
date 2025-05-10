from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))

    # Método para verificar a senha
    def check_password(self, password_plaintext):
        return check_password_hash(self.password, password_plaintext)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=True)
    responsavel_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    responsavel = db.relationship('User', backref=db.backref('projetos', lazy=True))
    