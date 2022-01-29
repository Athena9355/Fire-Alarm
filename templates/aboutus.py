# import "packages" from flask
from flask import Flask, render_template, request, Blueprint
import requests, json

from __init__ import app

# create a Flask instance

from templates.aadya_aboutme_api import get_numberfact
from templates.athena_aboutme_api import get_word
from templates.siya_aboutme_api import siya


from crud.app_crud import app_crud

app.register_blueprint(about_us)

about_us = Blueprint('about_us', __name__,
                     url_prefix='/crud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='assets')


@app.route('/aadya')
def aadya():
    return render_template("aadya.html")


@app.route('/nutritional_info_api', methods=['GET', 'POST'])
def search():
    result = ""
    if request.form:
        ingredient = request.form.get("search")
        result = get_info(ingredient)
        render_template("athena.html", result=result)  # works when nutrition.html is changed to athena.html
        # if len(input_word) == 0:  # no input
        # print("Please enter an input")
        # print(result)
    return render_template("athena.html", result=result)  # works when nutrition.html is changed to athena.html


@app.route('/athena')
def athena():
    return render_template("athena.html")



@app.route('/athena_aboutme_api', methods=['GET', 'POST'])
def define():
    result = ""
    if request.form:
        input_word = request.form.get("define")
        result = get_word(input_word)
        render_template("athena.html", result=result)
        # if len(input_word) == 0:  # no input
        # print("Please enter an input")
        # print(result)
    return render_template("athena.html", result=result)

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
    return render_template("siya.html", result=output)





