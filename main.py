# import "packages" from flask
from flask import Flask, render_template, request
import requests, json

# create a Flask instance
from templates.aadya_aboutme_api import get_numberfact
from templates.athena_aboutme_api import get_word

app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


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


@app.route('/recipes')
def recipes():
    return render_template("recipes.html")


@app.route('/menus')
def menus():
    return render_template("menus.html")


@app.route('/restaurants')
def restaurants():
    return render_template("restaurants.html")


@app.route('/About Us/')
def aboutus():
    return render_template("About Us.html")


@app.route('/asianfood')
def asianfood():
    return render_template("asianfood.html")


@app.route('/americanfood')
def americanfood():
    return render_template("americanfood.html")


@app.route('/europeanfood')
def europeanfood():
    return render_template("europeanfood.html")


@app.route('/mexicanfood')
def mexicanfood():
    return render_template("mexicanfood.html")


@app.route('/oceanicfood')
def oceanicfood():
    return render_template("oceanicfood.html")


@app.route('/aadya_aboutme_api', methods=['GET', 'POST'])
def api_translator():
    number = " "
    if request.form:
        english_text = request.form.get("translate")
        number = get_numberfact(english_text)
        if number != 0:  # input field has content
            print("Please enter an input")
        print(number)

    return render_template("aadya.html", fact=number)


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

@app.route('/about_us')
def about_us():
    return render_template("layouts/about_us.html")

@app.route('/aboutustemp')
def aboutustemp():
    return render_template("/aboutustemp.html")

@app.route('/pagelayout/index')
def pl():
    return render_template("pagelayout/index.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
