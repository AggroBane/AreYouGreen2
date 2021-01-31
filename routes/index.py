from . import routes
from flask import Flask, render_template

@routes.route('/')
def index():
    return render_template("index.html")
   
@routes.route('/login/')
def login():
    return render_template("login.html")
   