from flask import Flask
from dotenv import load_dotenv
from routes import *
import os
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit, join_room, send

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

socketio = SocketIO(app)

@socketio.on('joinOrganisation')
def joinOrganisation(orgId, username):
    # TODO: Check si le username fait partie de la room
    emit('newConnection', username, room=orgId)
    join_room(orgId)
    emit('connection')




if __name__ == '__main__':
    app.register_blueprint(routes)
    socketio.run(app, debug=True)

