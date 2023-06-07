from flask import Flask, redirect
from flask_login import LoginManager
from .models import User
from .routes import auth, main, api
from .config import app_config
from .database import init_db, db
import os

app = Flask(__name__)
if os.environ.get("FLASK_ENV") == "production":
    app.config.from_object(app_config["production"])
else:
    app.config.from_object(app_config["development"])


# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Inicializar la base de datos
init_db(app)
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(username):
    return User.get(username)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


# Registra las rutas de autenticación y principales
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run()
