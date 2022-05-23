import requests

endPoint = "https://pokeapi.co/api/v2/pokemon/22"

response = requests.get(endPoint)

bigDictionary = (response.json())

print(bigDictionary)

#print(bigDictionary["abilities"][0]["ability"]["name"])

for item in bigDictionary["abilities"]:
    print(item)

