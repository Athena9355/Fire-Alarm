import random

from flask import Blueprint

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')

food_data = []
food_list = [


                {"foodName":"Chicken Burrito", "foodType":"Burrito", "protein":"chicken", "calories":975},
                {"foodName":"Steak Burrito", "foodType":"Burrito", "protein":"steak", "calories":945},
                {"foodName":"Carnitas Burrito", "foodType":"Burrito", "protein":"carnitas", "calories":1005},
                {"foodName":"Barbacoa Burrito", "foodType":"Burrito", "protein":"barbacoa", "calories":965},
                {"foodName":"Chorizo Burrito", "foodType":"Burrito", "protein":"chorizo", "calories":1095},
                {"foodName":"Sofritas Burrito", "foodType":"Burrito", "protein":"sofritas", "calories":945},
                {"foodName":"Chicken Corn Tortilla Taco", "foodType":"Taco", "protein":"chicken", "calories":650},
                {"foodName":"Chicken Flour Tortilla Taco", "foodType":"Taco", "protein":"chicken", "calories":700},
                {"foodName":"Steak Corn Tortilla Taco", "foodType":"Taco", "protein":"steak", "calories":620},
                {"foodName":"Steak Flour Tortilla Taco", "foodType":"Taco", "protein":"steak", "calories":670},
                {"foodName":"Carnitas Corn Tortilla Taco", "foodType":"Taco", "protein":"carnitas", "calories":680},
                {"foodName":"Carnitas Flour Tortilla Taco", "foodType":"Taco", "protein":"carnitas", "calories":730},
                {"foodName":"Barbacoa Corn Tortilla Taco", "foodType":"Taco", "protein":"barbacoa", "calories":640},
                {"foodName":"Barbacoa Flour Tortilla Taco", "foodType":"Taco", "protein":"barbacoa", "calories":690},
                {"foodName":"Chorizo Corn Tortilla Taco", "foodType":"Taco", "protein":"chorizo", "calories":770},
                {"foodName":"Chorizo Flour Tortilla Taco", "foodType":"Taco", "protein":"chorizo", "calories":820},
                {"foodName":"Sofritas Corn Tortilla Taco", "foodType":"Taco", "protein":"sofritas", "calories":620},
                {"foodName":"Sofritas Flour Tortilla Taco", "foodType":"Taco", "protein":"sofritas", "calories":670},



]


def _init_food():
    item_id = 1
    for item in food_list:
        food_data.append({" ": item})
        item_id += 1




@app_api.route('/food')
def food1():
    if len(food_data) == 0:
        _init_food()
    return random.choice(food_data)




if __name__ == "__main__":
    print(random.choice(food_list))
