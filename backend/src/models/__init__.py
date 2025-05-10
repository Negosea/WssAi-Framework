
from flask_sqlalchemy import SQLAlchemy

# Cria a instância do banco de dados
db = SQLAlchemy()

# Importe todos os modelos aqui
from .user import User  # type: ignore # Ajuste se seu arquivo tiver outro nome

# Opcional: lista de modelos para facilitar imports
__all__ = ['db', 'User']
