# Copyright 2022 iiPython

# Modules
from flask_sqlalchemy import SQLAlchemy

# Initialization
db = SQLAlchemy()

# Models
class User(db.Model):
    userid = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)

class Post(db.Model):
    __bind_key__ = "posts"
    postid = db.Column(db.Integer, primary_key = True, unique = True)
    userid = db.Column(db.Integer)
    title = db.Column(db.String)
    content = db.Column(db.Text)
