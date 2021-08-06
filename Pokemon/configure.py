import pymysql
port_number = 3080
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokimon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)