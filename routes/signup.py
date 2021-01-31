from . import routes
from flask import Flask, render_template, request

@routes.route("/<orgId>/<userId>")
def orgIndex(orgId, userId):
    # Check if org exists in db
    return None