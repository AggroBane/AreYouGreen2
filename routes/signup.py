from . import routes
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db
from ModelImports import *

@routes.route("/create",  methods=['GET', 'POST'])
def orgCreate():
    if request.method == 'GET':
        return render_template("register.html")
    else :
        # Create org in database
        desiredName = request.form.get('orgId')
        print(desiredName)
        newOrg = Organisations(name = desiredName)
        db.session.add(newOrg)
        db.session.commit()
        return redirect('/create/' + request.form.get('orgId'))

@routes.route("/create/<orgId>")
def orgJoin(orgId):
    # Create new organisation!
    # TODO Create join page for organisation
    return 'This page is for the creation of an organisation'