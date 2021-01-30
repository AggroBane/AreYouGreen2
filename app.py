from flask import Flask
from routes import *
from flask_socketio import SocketIO, emit, join_room, send

app = Flask(__name__)
socketio = SocketIO(app)

rooms = {}

@socketio.on('joinOrganisation')
def joinOrganisation(orgId, username):
    # TODO: Check si le username fait partie de la room
    emit('newConnection', username, room=orgId)
    join_room(orgId)
    emit('connection')




if __name__ == '__main__':
    app.register_blueprint(routes)
    socketio.run(app, debug=True)