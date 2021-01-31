from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
PUBLIC_IP_ADDRESS = os.getenv('PUBLIC_IP_ADDRESS')
DBNAME = os.getenv('DBNAME')

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]= "db login string goes here"
db = SQLAlchemy(app)

db.create_all()
db.session.commit()

