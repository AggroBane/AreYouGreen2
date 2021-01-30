from . import routes
from flask import Flask, render_template, request


@routes.route("/organisation/<id>")

def orgInfo(id):

    name = request.args.get('name')

    return name