import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4ed21019c9be33af9ba8f1ac3beaa54e'
HEADERS = {'Content-Type : application/json'}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

respons = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_create)
print(respons.text)