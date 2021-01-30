from . import routes
from flask import Flask, render_template

@routes.route('/')
def index():
    #testCarte = mongo.db.cartes.find_one({"_id": "carte:1"})

    return testCarte["cue"]
   

