from . import routes
from flask import Flask, render_template
@routes.route("/test")
def test():
    return render_template('login.html')
