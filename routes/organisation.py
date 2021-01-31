from . import routes
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db
from ModelImports import *

@routes.route("/organisation/<orgId>")
def orgInfo(orgId):
    username = request.args.get('name')
    return render_template('organisation.html', username=username, orgId=orgId)

@routes.route("/organisation/<orgId>/stats")
def orgStats(orgId):
    username = request.args.get('name')
    return render_template('stats.html', username=username, orgId=orgId)

@routes.route("/coreApp/<orgId>/<usrname>")
def orgIndex(orgId, usrname):

    # Check if org exists
    org = Organisations.query.filter_by(name=orgId).first()

    if org is None :
        return redirect('/join')

    #Check if user exists in org
    usr = Users.query.join(Departments, Users.fk_department==Departments.id).join(Organisations, Departments.fk_orgName==Organisations.name).filter(Users.username == usrname).first()
    if usr is None :
        return 'user doesnt exist in org'

    deps = Departments.query.join(Organisations, Departments.fk_orgName==Organisations.name).join(Tasks, Departments.id==Tasks.fk_department).all()

    return render_template('organisationDbEnabled.html', user=usr, organisation=org, departments=deps)