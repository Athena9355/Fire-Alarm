#import "packages" from flask
from flask import Flask, render_template, request

#create a Flask instance
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
    return render_template("gaurish.html")

@app.route('/karthik')
def karthik():
    return render_template("karthik.html")

@app.route('/siya')
def siya():
    return render_template("siya.html")

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
def dictionary():
    result = " "
    if request.form:
        input_word = request.form.get("translate_word")
        result = get_word(input_word)
        render_template("athena.html", result=result)
        #if len(input_word) == 0:  # no input
        #print("Please enter an input")
        #print(result)
    #return render_template("athena.html", result=result)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
