import pymysql


def heaviest_pokemon():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        db="pokimon",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        query = "SELECT name FROM pokemon WHERE weight in (SELECT MAX(weight) FROM pokemon)"
        cursor.execute(query)
        result = cursor.fetchall()
    return result[0]['name']
print(heaviest_pokemon())