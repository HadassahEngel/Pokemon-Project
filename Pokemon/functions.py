import requests

from configure import connection

def get_id_by_name(name):
    sql = "select id from pokemon where name='{}'".format(name)
    return get_form_sql(sql)[0]["id"]

def get_data_form_server(my_url):
    res = requests.get(url=my_url, verify=False).json()
    return res

def get_from_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

def updata_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
        connection.close()

def put_in_DB(id,type):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO type (id_pokemon, type) VALUES" + str(
                (id,type))
            cursor.execute(sql)
        connection.commit()
    except: print("the insert this row: {},{} fail".format(id,type))


def put_pokemon(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
    connection.commit()


