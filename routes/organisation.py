from . import routes
from flask import Flask, render_template, request

@routes.route("/organisation/<orgId>")
def orgInfo(orgId):
    username = request.args.get('name')
    return render_template('organisation.html', username=username, orgId=orgId)

@routes.route("/organisation/<orgId>/stats")
def orgStats(orgId):
    username = request.args.get('name')
    return render_template('stats.html', username=username, orgId=orgId)
