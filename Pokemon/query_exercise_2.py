import pymysql


def find_by_type(grass):
    arrayToReturn = []
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        db="pokimon",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        try:
            query = "SELECT name from pokemon,type WHERE Type.Type='{}' and pokemon.id=Type.id_pokemon".format(grass)
            print(query)
            cursor.execute(query)
            result = cursor.fetchall()
        except: return "select fail"
        for i in result:
            arrayToReturn.append(i["name"])
    return arrayToReturn
print(find_by_type('venusaur'))