import os
import logging
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from flask_login import LoginManager, login_user, current_user, logout_user, login_required  # type: ignore
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# ================================================
# CONFIGURAÇÃO DO APP
# ================================================
app = Flask(__name__)
app.secret_key = "sua_chave_secreta_muito_forte_e_aleatoria"  # Troque por uma chave segura!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/wssai.db'  # Banco na pasta backend
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'backend/uploads'  # Pasta para uploads
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Cria a pasta se não existir

# ================================================
# EXTENSÕES
# ================================================
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Configuração de logs
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# ================================================
# MODELOS
# ================================================
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

# ================================================
# LOADER DE USUÁRIO
# ================================================
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ================================================
# ROTAS
# ================================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash("Email já registrado.", "error")
            return redirect(url_for('register'))

        new_user = User(nome=nome, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registro realizado com sucesso! Faça login.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Preencha todos os campos.", "error")
            return redirect(url_for('login'))

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
            
        flash("Email ou senha incorretos.", "error")
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu com sucesso.", "info")
    return redirect(url_for('login'))

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("Nenhum arquivo enviado.", "error")
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash("Nenhum arquivo selecionado.", "error")
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename) # type: ignore
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            try:
                # Adicione aqui seu processamento de PDF/Imagem
                # Exemplo genérico:
                if filename.lower().endswith(".pdf"):
                    # text = preprocess_pdf(file_path)
                    text = "Conteúdo processado do PDF"
                elif filename.lower().endswith((".jpg", ".jpeg", ".png")):
                    # text = process_image(file_path)
                    text = "Conteúdo processado da imagem"
                else:
                    flash("Formato não suportado.", "error")
                    return redirect(request.url)

                output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{os.path.splitext(filename)[0]}.txt")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                
                return render_template("result.html", text=text)
                
            except Exception as e:
                flash(f"Erro no processamento: {str(e)}", "error")
                return redirect(request.url)

    return render_template("upload.html")

# ================================================
# INICIALIZAÇÃO
# ================================================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria o banco e tabelas se não existirem
    app.run(debug=True)