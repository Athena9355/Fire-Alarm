from flask import Flask, render_template, Blueprint
import requests
import json
import random

from __init__ import app

aboutus = Blueprint('aboutus', __name__)

@app.route('/aadya')
def aadya():
    return render_template("aadya.html")



@app.route('/athena')
def athena():
    return render_template("athena.html")


@app.route('/gaurish')
def gaurish():

    url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

    headers = {
        'x-rapidapi-host': "jokes-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "9fb1283360mshedc514375b603d6p156a26jsna7cd4ca5744a"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    output = json.loads(response.text)
    return render_template("gaurish.html", result=output)

@app.route('/karthik')
def karthik():
    return render_template("karthik.html")




@app.route('/siya')
def siya():
    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"

    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "0a4557c36bmsh023bf219202e218p153360jsndbf67f2a9f06"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("siya.html", result = output)