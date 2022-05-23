import requests
from pprint import pprint

pokemon_number = input("What is the pokemon's ID?")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon["name"])

#ID = 7


