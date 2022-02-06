import random

from flask import Blueprint
from flask import Blueprint, render_template
from __init__ import app

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')
food_data_subway = []
food_list_subway = [
                       {"foodName":"Black Forest Ham", "calories":290 },
                       {"foodName":"Black Forrest Ham", "calories":290},
                       {"foodName":"Six inch Black Forest Ham", "calories":290},
                       {"foodName":"6 inch Black Forest Ham", "foodType":"Six inch", "calories":290},
                       {"foodName":"12 inch Black Forest Ham", "calories":580},
                       {"foodName":"Footlong Black Forest Ham", "foodType":"Footlong", "calories":580},
                       {"foodName":"Oven Roasted Chicken", "calories":320},
                       {"foodName":"6 inch Oven Roasted Chicken", "foodType":"Six inch", "calories":320},
                       {"foodName":"Six inch Oven Roasted Chicken", "calories":320},
                       {"foodName":"12 inch Oven Roasted Chicken", "calories":640},
                       {"foodName":"Footlong Oven Roasted Chicken", "foodType":"Footlong", "calories":640},
                       {"foodName":"6 inch Roast Beef", "foodType":"Six inch", "calories":320},
                       {"foodName":"Six inch Roast Beef", "calories":320},
                       {"foodName":"12 inch Roast Beef", "calories":640},
                       {"foodName":"Footlong Roast Beef", "foodType":"Footlong", "calories":640},
                       {"foodName":"Chicken and Bacon Ranch Melt", "foodType":"Chicken", "calories":590},
                       {"foodName":"Chicken Bacon Ranch Melt", "foodType":"Chicken", "calories":590},
                       {"foodName":"Cold Cut Combo", "calories":340},
                       {"foodName":"Cold Cut", "calories":340}
    ]
def _init_food_subway():
    item_id = 1
    for item in food_list_subway:
        food_data_subway.append({" ": item})
        item_id += 1
@app_api.route('/food_calorie_subway')
def food1_subway():
    if len(food_data_subway) == 0:
        _init_food_subway()
    return random.choice(food_data_subway)



@app.route('/food_calorie_subway_py', methods=['GET', 'POST'])
def py_calorie_subway():
    return render_template("food_calorie.html", result4=food1_subway())




if __name__ == "__main__":
    print(random.choice(food_list_subway))