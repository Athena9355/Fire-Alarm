import random

from flask import Blueprint
from flask import Blueprint, render_template
from __init__ import app

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')
food_data_paneera = []
food_list_paneera = [
                        {"foodName":"Tomato Mozzarella Flatbread", "calories":350, "carbs":35 },
                        {"foodName":"Roasted Turkey Cranberry Flatbread", "calories":310, "carbs":36 },
                        {"foodName":"Turkey Cranberry Flatbread", "calories":310, "carbs":36 },
                        {"foodName":"Half Size Italian on Hoagie Roll", "calories":440, "carbs":38 },
                        {"foodName":"Italian on Hoagie Roll", "calories":880, "carbs":75 },
                        {"foodName":"Steak and White Cheddar Panini", "calories":940, "carbs":79 },
                        {"foodName":"Half Size Chicken Panini", "calories":380, "carbs":42 },
                        {"foodName":"Frontega Chicken Panini on Focaccia", "calories":750, "carbs":85 },
                        {"foodName":"Half Size Turkey Breast Sandwich", "calories":280, "carbs":32 },
                        {"foodName":"Turkey Breast Sandwich", "calories":560, "carbs":65},
                        {"foodName":"Classic Grilled Cheese", "calories":640, "carbs":73 },
                        {"foodName":"Half Size Classic Grilled Cheese", "calories":320, "carbs":37 },
                        {"foodName":"Chicken Salad Sandwich", "calories":700, "carbs":90},
                        {"foodName":"Veggie Sandwich", "calories":440, "carbs":65},
                        {"foodName":"Small Mac and Cheese", "calories":470, "carbs":36},
                        {"foodName":"Kids Mac and Cheese", "calories":470, "carbs":36},
                        {"foodName":"Large Mac and Cheese", "calories":950, "carbs":71},
                        {"foodName":"Mac and Cheese Breadbowl", "calories":1140, "carbs":166}
]
def _init_food_paneera():
    item_id = 1
    for item in food_list_paneera:
        food_data_paneera.append({" ": item})
        item_id += 1
@app_api.route('/food_calorie_paneera')
def food1_paneera():
    if len(food_data_paneera) == 0:
        _init_food_paneera()
    return random.choice(food_data_paneera)


@app.route('/food_calorie_paneera_py', methods=['GET', 'POST'])
def py_calorie_paneera():
    return render_template("food_calorie.html", result2=food1_paneera())




if __name__ == "__main__":
    print(random.choice(food_list_paneera))