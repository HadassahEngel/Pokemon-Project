from urllib import request

import pymysql
from configure import connection
import functions


def service_update_types(pokimon_name):
    url_get_pokmon = "https://pokeapi.co/api/v2/pokemon/{}".format(pokimon_name)
    res = functions.get_data_form_server(url_get_pokmon)
    arrayTepes = res["types"]
    allTypes = []
    for i in arrayTepes:
        allTypes.append(i["type"]["name"])
        try:
            id = functions.get_id_by_name(pokimon_name)
        except:
            return ["update type fail", 400]
        for i in allTypes:
            try:
                functions.put_in_DB(id, i)
            except pymysql.err.IntegrityError:
                return ["this type for this pokemon already exist in the sqk", 400]
            except:
                print("this is update type fail")
    return ["update type Succeeded", 200]


def service_update_evolve(pokemon,trainer):
    try:
        id_pokemon= functions.get_id_by_name(pokemon)
    except: print("There is no such name of pokimon",400)
    url='https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon)
    url_from_species = functions.get_data_form_server(url)["species"]["url"]
    url_chein= functions.get_data_form_server(url_from_species)["evolution_chain"]["url"]
    evolution_chain = functions.get_data_form_server(url_chein)["chain"]
    print(evolution_chain["evolves_to"])
    if evolution_chain["evolves_to"]==[]:
        return ["this pokemon con't evolve",200]
    while evolution_chain["evolves_to"]!=[]:
        evolution_chain=evolution_chain["evolves_to"][0]
    my_name_evolve=evolution_chain["species"]["name"]
    try:
        id_evolve= functions.get_id_by_name(my_name_evolve)
    except: print("did not find id of the evolve pokemon")
    try:
        sql="select * from ownedBy where name_owner='{}' and id_pokemon={}".format(trainer,id_evolve)
        theRow= functions.get_from_sql(sql)
    except: return ["select fail",400]
    print(theRow)
    if theRow==():
        return ["This pokemon doesn't have this trainar",400]
    my_update="UPDATE ownedBy SET name_owner = '{}' , id_pokemon = {} WHERE name_owner='{}' and id_pokemon={}".format(trainer,id_evolve,trainer,id_pokemon)
    try:
        functions.updata_sql(my_update)
    except pymysql.err.ProgrammingError as err:
        return [err, 400]
    except pymysql.err.IntegrityError:
        return ["this update alerdy exist",400]
    except: return ["update evolve fail", 400]
    return ["update evolve succeeded",200]

def service_add_pokemon(new_pokemon):
    sql = "INSERT INTO pokemon (id, name, height, weight) VALUES" + str((new_pokemon["id"], new_pokemon["name"], \
                                                                         new_pokemon["height"], new_pokemon["weight"]))
    try:
        functions.put_pokemon(sql)
    except pymysql.err.IntegrityError:
        return ["exist a pokemon with this id", 400]
    except pymysql.err.ProgrammingError as a:
        return [a, 422]
    except:
        return ["post pokemon fail", 400]
    for type in new_pokemon["types"]:
        try:
            functions.put_in_DB(new_pokemon["id"], type)
        except:
            return ["post pokemon (type) fail", 400]
    return ["add pokemon Succeeded", 200]


def service_get_pokemons_by_type(type):
    arrayToReturn = []
    query = f"SELECT name FROM pokemon, type Where id=id_pokemon AND type='{type}'"
    try:
        result = functions.get_from_sql(query)
        for i in result:
            arrayToReturn.append(i["name"])
        return [arrayToReturn,200]
    except:
        return["get_pokemons_by_type fail",400]
def service_get_pokemons_by_trainer(name_owners):
    arrayToReturn = []
    query = f"SELECT name FROM pokemon, ownedBy Where id=id_pokemon AND name_owner='{name_owners}'"
    try:
        result = functions.get_from_sql(query)
        for i in result:
            arrayToReturn.append(i["name"])
        return [arrayToReturn,200]
    except:
        return["get_pokemons_by_trainer fail",400]

print(service_get_pokemons_by_trainer("Misty"))
def service_get_trainers_of_to_pokemon(pokemon):
    arrayToReturn = []
    query = f"SELECT name_owner FROM pokemon, ownedBy Where id=id_pokemon AND name='{pokemon}'"
    try:
        result = functions.get_from_sql(query)
        for i in result:
            arrayToReturn.append(i["name_owner"])
        return [arrayToReturn,200]
    except:
        return ["get_trainers_of_to_pokemon fail",400]
def service_delete_pokemon(id_pokemon):
    mycursor = connection.cursor()
    query = f"DELETE from type where id_pokemon='{id_pokemon}'"
    try:
        mycursor.execute(query)
        connection.commit()
    except:
        return ["delete from type is fail",400]
    query = f"DELETE from ownedBy where id_pokemon='{id_pokemon}'"
    try:
        mycursor.execute(query)
        connection.commit()
    except:
        return ["delete from ownedBy is fail",400]
    query = f"DELETE from pokemon where id='{id_pokemon}'"
    try:
        mycursor.execute(query)
        connection.commit()
        return ["delete ",200]
    except:
        return ["delete from pokemon is fail",400]
