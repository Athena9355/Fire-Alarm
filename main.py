from flask import render_template, request
import requests, json

from __init__ import app

# create a Flask instance

from templates.aadya_aboutme_api import get_numberfact
from templates.ordering_menus.inandout import tax_calculator

#PLEASE DO NOT DELETE THESE: blue print doesn't work, even if these are not being called, however they are
# needed for the calorie function.


from templates.nutritional_info_api import get_info
#from api.webapi import app_api

from crud.app_crud import app_crud

app.register_blueprint(app_crud)
#app.register_blueprint(app_api)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipes')
def recipes():
    return render_template("recipes.html")

@app.route('/result_recipe_rice')
def result_recipe_rice():
    return render_template("result_recipe_rice.html")

@app.route('/result_recipe_potatos')
def result_recipe_potatos():
    return render_template("result_recipe_potatos.html")

@app.route('/result_recipe_pm')
def result_recipe_pm():
    return render_template("result_recipe_pm.html")

@app.route('/result_recipe_rm')
def result_recipe_rm():
    return render_template("result_recipe_rm.html")

@app.route('/result_recipe_rp')
def result_recipe_rp():
    return render_template("result_recipe_rp.html")

@app.route('/result_recipe_all')
def result_recipe_all():
    return render_template("result_recipe_all.html")



@app.route('/restaurants')
def restaurants():
    return render_template("Restaurant Generator/restaurants.html")

@app.route('/wacky')
def wacky():
    return render_template("wacky.html")

@app.route('/About Us/')
def aboutus():
    return render_template("About Us.html")


@app.route('/asianfood')
def asianfood():
    return render_template("Restaurant Generator/asianfood.html")

@app.route('/asianfoodgen')
def asianfoodgen():
    return render_template("Restaurant Generator/asianfoodgen.html")


@app.route('/americanfood')
def americanfood():
    return render_template("Restaurant Generator/americanfood.html")

@app.route('/americanfoodgen')
def americanfoodgen():
    return render_template("Restaurant Generator/americanfoodgen.html")


@app.route('/europeanfood')
def europeanfood():
    return render_template("Restaurant Generator/europeanfood.html")

@app.route('/europeanfoodgen')
def europeanfoodgen():
    return render_template("Restaurant Generator/europeanfoodgen.html")


@app.route('/oceanicfood')
def oceanicfood():
    return render_template("Restaurant Generator/oceanicfood.html")

@app.route('/oceanicfoodgen')
def oceanicfoodgen():
    return render_template("Restaurant Generator/oceanicfoodgen.html")


@app.route('/foodgallery')
def foodgallery():
    return render_template("foodgallery.html")

@app.route('/about_us')
def about_us():
    return render_template("layouts/about_us.html")

@app.route('/fetch')
def fetch():
    return render_template("fetch.html")

@app.route('/aboutustemp')
def aboutustemp():
    return render_template("/aboutustemp.html")


@app.route('/pagelayout/index')
def pl():
    return render_template("pagelayout/index.html")

##nutritional information api

@app.route('/nutrition')
def nutrition():
    return render_template("nutrition.html")

@app.route('/locationfinder')
def locationfinder():
    return render_template("locationfinder.html")

@app.route('/reservation')
def reservation():
    return render_template("reservation.html")



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

@app.route('/darkmode')
def darkmode():
    return render_template("darkmode.html")

@app.route('/snakegame')
def snakegame():
    return render_template("snakegame.html")

@app.route('/pacman')
def pacman():
    return render_template("PacMan Game/index.html")


@app.route('/pacman2')
def pacman2():
    return render_template("PacMan ver 2/pacman2.html")




@app.route('/aadya')
def aadya():
    return render_template("aadya.html")

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



@app.route('/food_calorie')
def calorie():
    return render_template("food_calorie.html")

@app.route('/athena')
def athena():
    return render_template("athena.html")



@app.route('/karthik')
def karthik():
    return render_template("karthik.html")


@app.route('/siya')
def siya():
    return render_template("siya.html")
    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"

    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "0a4557c36bmsh023bf219202e218p153360jsndbf67f2a9f06"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("siya.html", result = output)




@app.route('/menus')
def menus():
    return render_template("menus.html")


@app.route('/inandout')
def inandout():
    return render_template("ordering_menus/inandout.html")


@app.route('/inandout', methods=['POST'])
def inandout_function():
    bill_final = " "
    if request.form:
        bill_amt = request.form.get("bill_html")
        bill_final = tax_calculator(bill_amt)
        if bill_amt != 0:  # input field has content
            print("Please enter an input")
        print(bill_final)
    return render_template("ordering_menus/inandout.html", final=bill_final)

@app.route('/kfc')
def kfc():
    return render_template("ordering_menus/kfc.html")


@app.route('/kfc', methods=['POST'])
def kfc_function():
    bill_final = " "
    if request.form:
        bill_amt = request.form.get("bill_html")
        bill_final = tax_calculator(bill_amt)
        if bill_amt != 0:  # input field has content
            print("Please enter an input")
        print(bill_final)
    return render_template("ordering_menus/kfc.html", final=bill_final)









# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
