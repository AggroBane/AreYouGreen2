from flask import Flask
from mongoengine import *
from routes import *

app = Flask(__name__)

connect(host="mongodb+srv://tp3-prog-web:rqXafz9SIAzghRC0@tp3-prog-web.8hzbi.mongodb.net/tp3-prog-web?retryWrites=true&w=majority")

if __name__ == '__main__':
    app.register_blueprint(routes)
    app.run(debug=True)