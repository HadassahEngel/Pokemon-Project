import json

import pymysql
import requests
import functions
from flask import Flask, Response, request

from service import service_update_types, service_update_evolve, service_add_pokemon, service_get_pokemons_by_type, \
    service_get_pokemons_by_trainer, service_get_trainers_of_to_pokemon, service_delete_pokemon

app = Flask(__name__)


@app.route('/update_types')
def update_types():
    pokimon_name = request.args.get('name')
    response=service_update_types(pokimon_name)
    return Response(response[0],response[1])

@app.route('/update_evolve', methods=['PUT'])
def update_evolve():
    body_get = request.get_json()
    pokemon=body_get["pokemon"]
    trainer=body_get["trainer"]
    return_ans=service_update_evolve(pokemon,trainer)
    return Response(return_ans[0],return_ans[1])

@app.route('/create_pokemon',methods=['POST'])
def add_pokemon():
    new_pokemon = request.get_json()
    return_ans=service_add_pokemon(new_pokemon)
    return Response(return_ans[0],return_ans[1])


@app.route('/get_pokemons_by_type/<type>')
def get_pokemons_by_type(type):
    result = json.dumps(service_get_pokemons_by_type(type))
    return Response(result)


@app.route('/get_pokemons_by_trainer/<name_owners>')
def get_pokemons_by_trainer(name_owners):
    result = service_get_pokemons_by_trainer(name_owners)
    if result[1]==200:
        return Response(json.dumps(result[0]),result[1])
    return Response(result[0],result[1])

@app.route('/get_triners_of_to_pokemon/<pokemon>')
def get_trainers_of_to_pokemon(pokemon):
    result = service_get_trainers_of_to_pokemon(pokemon)
    if result[1] == 200:
        return Response(json.dumps(result[0]), result[1])
    return Response(result[0], result[1])


@app.route('/delete_pokemon/<id_pokemon>', methods=['DELETE'])
def delete_pokemon(id_pokemon):
    service_delete_pokemon(id_pokemon)
    return Response()





