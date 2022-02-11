from flask import Flask, render_template, Blueprint
import requests
import json

from __init__ import app

search = Blueprint('search', __name__)

@app.route('/searchmeals')
def searchmeals():
    return render_template("searchmeals/searchfile.html")