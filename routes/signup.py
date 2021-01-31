from . import routes
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import db
from ModelImports import *

@routes.route("/create")
def orgCreate():
    # Create new organisation!
    # TODO Create signup page => redirect to create/orgId
    return

@routes.route("/create/<orgId>")
def orgJoin(orgId):
    # Create new organisation!
    # TODO Create join page for organisation
    return 'This page is for the creation of an organisation'