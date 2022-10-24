# Copyright 2022 iiPython

# Modules
from flask import Flask
from flask_session import Session

from .dbschema import db

# Initialization
app = Flask("shuttle")

# Flask SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///../data/db/userdata.db"
app.config["SQLALCHEMY_BINDS"] = {
    "posts": "sqlite:///../data/db/posts.db"
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

# Flask Session
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db

s = Session(app)

# Create databases
with app.app_context():
    s.app.session_interface.db.create_all()
    db.create_all()

# Blueprints
from shuttle.blueprints.auth import auth
app.register_blueprint(auth)
