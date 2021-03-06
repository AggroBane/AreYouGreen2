from . import routes
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import db
from ModelImports import *

@routes.route("/organisation/<orgId>/<usrname>/stats")
def orgStats(orgId, usrname):
    # Check if org exists
    org = Organisations.query.filter_by(name=orgId).first()

    if org is None :
        return redirect('/join')

    #Check if user exists in org
    usr = Users.query.join(Departments, Users.fk_department==Departments.id).join(Organisations, Departments.fk_orgName==Organisations.name).filter(Users.username == usrname).first()
    if usr is None :
        return 'user doesnt exist in org'
        
    return render_template('stats.html', user=usr, org=org)

@routes.route("/organisation/<orgId>/<usrname>")
def orgIndex(orgId, usrname):

    # Check if org exists
    org = Organisations.query.filter_by(name=orgId).first()

    if org is None :
        return redirect('/join')

    #Check if user exists in org
    usr = Users.query.join(Departments, Users.fk_department==Departments.id).join(Organisations, Departments.fk_orgName==Organisations.name).filter(Users.username == usrname).first()
    if usr is None :
        return 'user doesnt exist in org'

    tabs = Departments.query.join(Organisations, Departments.fk_orgName==Organisations.name).join(Tasks, Departments.id==Tasks.fk_department).all()

    tempData = {}

    for tab in tabs:
        tabTasks = Tasks.query.filter_by(fk_department=tab.id).all()
        tempData[tab.name] = {}

        for task in tabTasks:
            tempData[tab.name][task.name] = [task.checked, task.description]

    return render_template('organisationDbEnabled.html', user=usr, org=org, tempData=tempData)