import requests

ingredient = input('Enter an ingredient: ')

app_id = "49e98703"
app_key = "f32fd862acb81bbbd93040e60c978dd4"
api_url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, app_id, app_key)
response = requests.get(api_url)
ret_recipe = (response.json())

def recipe_search(ingredient):
    return ret_recipe['hits']
#print(ret_recipe['hits'])

for item in ret_recipe['hits']:
    recipe = item["recipe"]
    print("Recipe: ", recipe["label"])
    print(recipe["url"])
    print("Ingredients: ")

    for ing in (recipe['ingredientLines']):
        print(ing)
    print(' ')





