import requests

##API source: https://rapidapi.com/edamam/api/edamam-food-and-grocery-database/
def get_info(ingredient):
    ingredient = str(ingredient)
    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

    querystring = {"ingr": ingredient}

    headers = {
        'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com",
        'x-rapidapi-key': "53c0bdc20bmshd40bff3eddbed53p11401djsn6beee195a713"
    }

    information = requests.request("GET", url, headers=headers, params=querystring)
    return information.text
