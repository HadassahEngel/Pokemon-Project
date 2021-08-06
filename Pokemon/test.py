import pytest
import requests
from query_exercise_2 import find_by_type

def test_update_type():
    url= "http://127.0.0.1:3080/update_types?name=venusaur"
    update_type = requests.get(url=url, verify=False)
    pokemon_of_type_poison=find_by_type('poison')
    pokemon_of_type_grass = find_by_type('grass')
    assert 'venusaur' in pokemon_of_type_poison
    assert 'venusaur' in pokemon_of_type_grass

def test_get_pokemon_by_type():
    assert 'eevee' in find_by_type('normal')
    url = "http://127.0.0.1:3080/update_types?name=eevee"
    update_type = requests.get(url=url, verify=False)
    arr= find_by_type('normal')
    arr.remove('eevee')
    assert 'eevee' not in arr

def test_add_pokemon():
    url="http://127.0.0.1:3080/create_pokemon"
    result_from_add_pokemon = requests.post(url, json={'id':193,'name':'yanma','height':12,'weight':380,'types':['bug' ,'flying']})
    assert 'yanma' in find_by_type('bug')
    assert 'yanma' in find_by_type('flying')
    try_agein = requests.post(url, json={'id': 193, 'name': 'yanma', 'height': 12, 'weight': 380, 'types': ['bug', 'flying']})

def test_get_pokemons_by_trainer():
    url="http://127.0.0.1:3080/get_pokemons_by_trainer/Drasna"
    result=requests.get(url=url, verify=False)
    assert result.json() == ["wartortle", "caterpie", "beedrill", "arbok", "clefairy", "wigglytuff", "persian",
                          "growlithe", "machamp", "golem", "dodrio", "hypno", "cubone", "eevee", "kabutops"]

def test_get_trainers_of_to_pokemon():
    url=("http://127.0.0.1:3080/get_triners_of_to_pokemon/charmander")
    result=requests.get(url=url, verify=False)
    assert result.json() == ["Giovanni", "Jasmine", "Whitney"]