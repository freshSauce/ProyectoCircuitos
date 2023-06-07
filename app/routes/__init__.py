from flask import Blueprint, render_template, request, redirect, send_file
from flask_login import login_user, logout_user, current_user, login_required
from ..models import User
from ..database import db, firebase_db
import os
from time import sleep

auth = Blueprint("auth", __name__)
main = Blueprint("main", __name__)
api = Blueprint("api", __name__)

database = firebase_db.Firebase()


@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form["inputEmail"]
        password = request.form["inputPassword"]
        remember = bool(
            request.form.get("remember")
        )  # Verificar si se seleccionó "Recuérdame"

        user = User.get(username)
        if user and user.check_password(password):
            login_user(user, remember=remember)

            return redirect("/")
        else:
            error_message = "Credenciales inválidas. Por favor, inténtalo nuevamente."
            return render_template(
                "auth/login.html",
                error_message=error_message,
                title="Inicio de Sesión - ITSPA",
            )

    return render_template("auth/login.html", title="Inicio de Sesión - ITSPA")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/login")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form["inputEmail"]
        password = request.form["inputPassword"]
        password2 = request.form["inputPassword2"]

        if password != password2:
            error_message = (
                "Las contraseñas no coinciden. Por favor, inténtalo nuevamente."
            )
            return render_template(
                "auth/register.html",
                error_message=error_message,
                title="Registro - ITSPA",
            )

        user = User.get(username)
        if user:
            error_message = (
                "El nombre de usuario ya está en uso. Por favor, inténtalo nuevamente."
            )
            return render_template(
                "auth/register.html",
                error_message=error_message,
                title="Registro - ITSPA",
            )

        User.create_user(username, password)
        return redirect("/login")

    return render_template("auth/register.html", title="Registro - ITSPA")


@main.route("/")
@login_required
def index():
    current = int(request.args.get("page", 0))
    quantity = int(request.args.get("quantity", 15))
    pages = list(database.pagination(quantity))
    data = pages[current].values()
    return render_template("index.html", title="Lista - ITSPA", data=data, pages=list(range(len(pages))), current=current)

@login_required
@api.route("/api/remove_access", methods=["POST"])
def remove_access():
    if current_user.is_authenticated:
        if current_user.username == "nex0loke@gmail.com":
            username = request.form["username"]
            user = User.get(username)
            if user:
                db.session.delete(user)
                db.session.commit()
                return {"message": f"User {username} removed succesfully"}, 200
            else:
                return {"message": f"User {username} not found"}, 404
            
@api.route("/api/get_list", methods=["GET"])
def get_list():
    pages = int(request.args["pages"])
    data = list(database.pagination(pages))

    return {"data": data, "pages": len(data)}, 200

@api.route("/api/export", methods=["GET"])
def export():
    # Generar el archivo Excel
    filename = database.export_to_excel()

    # Obtener el archivo Excel generado
    excel_file = filename

    # Enviar el archivo como Blob

    return send_file(excel_file, as_attachment=True, download_name='pase_de_lista.xlsx')
    

