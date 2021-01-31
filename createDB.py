from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
PUBLIC_IP_ADDRESS = os.getenv('PUBLIC_IP_ADDRESS')
DBNAME = os.getenv('DBNAME')

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]= insertRouteHere
db = SQLAlchemy(app)

class Owner(db.Model):
    username = db.Column(db.String(50), nullable = False, primary_key = True)
    organisations = db.relationship('Organisations', backref='owner')

class Organisations(db.Model):
    name = db.Column(db.String(50), nullable=False, primary_key=True)
    fk_owner = db.Column(db.String(50), db.ForeignKey('owner.username'))
    departments = db.relationship('Departments', backref='organisation')

class Departments(db.Model):
    name = db.Column(db.String(50), nullable = False, primary_key = True)
    fk_orgName = db.Column(db.String(50), db.ForeignKey('organisations.name'))
    users = db.relationship('Users', backref='department')

class Users(db.Model):
    username = db.Column(db.String(50), nullable = False, primary_key = True)
    fk_department = db.Column(db.String(50), db.ForeignKey('departments.name'), nullable=True)
    tasks = db.relationship('Tasks', backref='user')
    tasks = db.relationship('Collabs', backref='user')

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(128), nullable = True)
    checked = db.Column(db.Boolean, default=False)
    fk_assignedUser = db.Column(db.String(50), db.ForeignKey('users.username'))
    fk_department = db.Column(db.String(50), db.ForeignKey('departments.name'))
    collaborators = db.relationship('Collabs', backref='task')

class Collabs(db.Model):
    fk_user = db.Column(db.String(50), db.ForeignKey('users.username'), primary_key = True)
    fk_task = db.Column(db.Integer, db.ForeignKey('tasks.id'), primary_key = True)







db.create_all()
db.session.commit()

