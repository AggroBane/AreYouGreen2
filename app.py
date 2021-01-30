from flask import Flask
from dotenv import load_dotenv
from routes import *
import os
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
PUBLIC_IP_ADDRESS = os.getenv('PUBLIC_IP_ADDRESS')
DBNAME = os.getenv('DBNAME')
  
# configuration 
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
  
db = SQLAlchemy(app) 
  
# User ORM for SQLAlchemy 
class User(db.Model): 
    username = db.Column(db.String(50), nullable = False, primary_key = True)

smallPepi = User(username = "smallPepi")


print(User.query.filter_by(username = "smallPepi").first())

socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

if __name__ == '__main__':
    app.register_blueprint(routes)
    socketio.run(app, debug=True)

