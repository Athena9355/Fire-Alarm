import random

from flask import Blueprint

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
    {"foodName":"Rotisserie-Style Chicken", "calories":350},
    {"foodName":"Roasted Chicken", "calories":350},
    {"foodName":"Rotisserie Chicken", "foodType":"Chicken", "calories":350},
    {"foodName":"6 inch Rotisserie Chicken", "foodType":"Six inch", "calories":350},
    {"foodName":"Six inch Rotisserie Chicken", "calories":350},
    {"foodName":"12 inch Rotisserie Chicken", "calories":700},
    {"foodName":"Footlong Rotisserie Chicken", "foodType":"Footlong", "calories":700},
    {"foodName":"Rotisserie Chicken Sandwich", "calories":350},
    {"foodName":"Subway Club", "calories":310},
    {"foodName":"6 inch Subway Club", "foodType":"Six inch", "calories":310},
    {"foodName":"12 inch Subway Club", "calories":620},
    {"foodName":"Footlong Subway Club", "calories":620},

    {"foodName":"6 inch Sweet Onion Chicken Teriyaki", "foodType":"Six inch", "calories":370},
    {"foodName":"12 inch Sweet Onion Chicken Teriyaki", "calories":740},
    {"foodName":"Footlong Teriyaki Chicken", "calories":740},
    {"foodName":"Footlong Sweet Onion Chicken Teriyaki", "calories":740},
    {"foodName":"Turkey Breast", "foodType":"Turkey", "calories":280, "correctedTerm":"6 inch Turkey Breast" },
    {"foodName":"6 inch Turkey and Cheese", "calories":280},
    {"foodName":"Six inch Turkey and Cheese", "calories":280},
    {"foodName":"6 inch Turkey Breast", "foodType":"Six inch", "calories":280},
    {"foodName":"12 inch Turkey Breast", "calories":560},
    {"foodName":"Footlong Turkey Breast", "calories":560},

    {"foodName":"12 inch Veggie Delite", "calories":560},
    {"foodName":"Footlong Veggie Delite", "calories":560},
    {"foodName":"Carved Turkey", "foodType":"Turkey", "calories":330},
    {"foodName":"6 inch Carved Turkey", "foodType":"Turkey", "calories":330},
    {"foodName":"12 inch Carved Turkey", "foodType":"Turkey", "calories":660},
    {"foodName":"Footlong Carved Turkey", "foodType":"Turkey", "calories":660},
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




if __name__ == "__main__":
    print(random.choice(food_list_subway))
