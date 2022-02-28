import random

from flask import Blueprint
from flask import Blueprint, render_template
from __init__ import app

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')
food_data_chickfila = []
food_list_chickfila = [
                          {"foodName":"Chicken Sandwich", "foodType":"Chicken", "calories":440},
                          {"foodName":"Chicken Deluxe Sandwich", "calories":500},
                          {"foodName":"Chicken Deluxe", "foodType":"Chicken", "calories":500},
                          {"foodName":"Spicy Chicken Deluxe Sandwich", "calories":570},
                          {"foodName":"Spicy Chicken Deluxe", "foodType":"Chicken", "calories":570},
                          {"foodName":"Spicy Deluxe", "calories":570},
                          {"foodName":"Spicy Deluxe Sandwich", "calories":570},
                          {"foodName":"Spicy Deluxe Chicken Sandwich", "calories":570},
                          {"foodName":"Chicken Salad Sandwich", "foodType":"Chicken", "calories":500},
                          {"foodName":"Spicy Chicken Sandwich", "calories":490},
                          {"foodName":"Spicy Chicken", "foodType":"Chicken", "calories":490},
                          {"foodName":"Grilled Chicken Sandwich", "calories":320},
                          {"foodName":"Grilled Chicken", "foodType":"Chicken", "calories":320},
                          {"foodName":"Four count Chicken Strips", "calories":470},
                          {"foodName":"Chick-n-Strips three piece", "calories":360},
                          {"foodName":"Grilled Chicken Club Sandwich", "calories":440},
                          {"foodName":"Grilled Chicken Club", "calories":440},
                          {"foodName":"12 piece chicken nuggets", "foodType":"Nuggets", "calories":400},
                          {"foodName":"Grilled Chicken Cool Wrap", "calories":340},
]
def _init_food_chickfila():
    item_id = 1
    for item in food_list_chickfila:
        food_data_chickfila.append({" ": item})
        item_id += 1
@app_api.route('/food_calorie_chickfila')
def food1_chickfila():
    if len(food_data_chickfila) == 0:
        _init_food_chickfila()
    return random.choice(food_data_chickfila)

@app.route('/food_calorie_chickfila_py', methods=['GET', 'POST'])
def py_calorie_chickfila():
    return render_template("food_calorie.html", result3=food1_chickfila())



if __name__ == "__main__":
    print(random.choice(food_list_chickfila))

