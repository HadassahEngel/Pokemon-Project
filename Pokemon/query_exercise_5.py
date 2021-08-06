import pymysql


def   finds_most_owned() :
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
        query = "SELECT name from pokemon WHERE id in(SELECT id_pokemon from (SELECT count(*) as amount, id_pokemon from ownedBy GROUP BY id_pokemon) as help WHERE amount=(SELECT max(amount) from (SELECT count(*) as amount, id_pokemon from ownedBy GROUP BY id_pokemon) as help));"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            arrayToReturn.append(i["name"])
    return arrayToReturn
print(finds_most_owned())