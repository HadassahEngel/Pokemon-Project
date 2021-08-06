import pymysql


def find_owners(name) :
    arrayToReturn=[]
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        db="pokimon",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        query = "SELECT ownedBy.name_owner from pokemon,ownedBy WHERE pokemon.id=ownedBy.id_pokemon and pokemon.name='{}';".format(name)
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            arrayToReturn.append(i["name_owner"])
    return arrayToReturn
print(find_owners('porygon'))