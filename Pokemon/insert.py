import pymysql
import json

def insert():
    f = open('pokemon_data.json','r')
    data = json.load(f)
    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokimon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
    )
    dictCheck={}
    for pokemon in data:
        try:
            with connection.cursor() as cursor:

                sql = "INSERT INTO pokemon (id, name, height, weight) VALUES"+str((pokemon["id"],pokemon["name"],pokemon["height"],pokemon["weight"]))
                cursor.execute(sql)
                connection.commit()
        except: print("row did not enter the table pokemon")
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO type (id_pokemon, type) VALUES"+str((pokemon["id"],pokemon["type"],))
                cursor.execute(sql)
                connection.commit()
        except: print("row did not enter the table type")
        for owner in pokemon['ownedBy']:
            try:
                with connection.cursor() as cursor:
                    if owner['name'] not in dictCheck:
                        query = "INSERT INTO owners (name, town) VALUES "+str((owner['name'], owner['town']))
                        dictCheck.update({owner['name']:owner['town']})
                        cursor.execute(query)
                        connection.commit()
            except: print("row did not enter the table owners")
            try:
                with connection.cursor() as cursor:
                    vals = (owner['name'], pokemon['id'])
                    query = "INSERT INTO ownedBy (name_owner, id_pokemon) VALUES"+str(vals)
                    cursor.execute(query)
                    connection.commit()
            except: print("row did not enter the table ownedBy")
insert()