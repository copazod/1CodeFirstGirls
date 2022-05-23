import requests
ingredient = input('Enter an ingredient: ')


app_id = "49e98703"
app_key = "f32fd862acb81bbbd93040e60c978dd4"

api_url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, app_id, app_key)
response = requests.get(api_url)
ret_recipe = response.json()
print(ret_recipe)




