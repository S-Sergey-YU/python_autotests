import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'de4828625696701ae787c1eb2aa7cbd9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
'Создание покемона'
body_create = {
    "name": "Тигр",
    "photo_id": "141"
}

respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create.status_code)
print(respons_create.text)
'Переименовать покемона'
body_new_name = {
    "pokemon_id": "370111",
    "name": "Левчик",
    "photo_id": 293
}

respons_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(respons_create.status_code)
print(respons_create.text)
'Поймать покемона'
body_add_pokeball = {
    "pokemon_id": "370111"
}

respons_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(respons_create.status_code)
print(respons_create.text)
'Провести битву'
body_battle = {
    "attacking_pokemon": "370111",
    "defending_pokemon": "370107"
}

respons_create = requests.post(url = f'{URL}/battle', headers = HEADER, json = body_battle)
print(respons_create.status_code)
print(respons_create.text)