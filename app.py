from flask import Flask
from routes import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

if __name__ == '__main__':
    app.register_blueprint(routes)
    socketio.run(app, debug=True)