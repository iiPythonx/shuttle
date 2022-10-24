# Copyright 2022 iiPython

# Modules
from flask import (
    abort, render_template,
    Blueprint
)
from shuttle import app, db

# Blueprint initialization
auth = Blueprint("auth", "shuttle.blueprints.auth", template_folder = "templates")

# Routes
@auth.route("/auth", methods = ["GET"])
def index() -> None:
    return render_template("welcome.html"), 200

@auth.route("/login", methods = ["GET", "POST"])
def login() -> None:
    return render_template("login.html"), 200

@auth.route("/register", methods = ["GET", "POST"])
def register() -> None:
    return render_template("register.html"), 200
