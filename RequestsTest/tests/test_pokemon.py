import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '39134'

def test_status_code_trainer():
    response = requests.get(url = f'{URL}/me/', headers = HEADER)
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url = f'{URL}/me/', headers = HEADER)

    assert response_get.json()['data'][0]['trainer_name'] == 'Баунти'
