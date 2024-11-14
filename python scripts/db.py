from getpass import getpass
from mysql.connector import connect, Error

connection = None
try:
    connection = connect(
        host="localhost",
        user='root',
        password='sqlpass',
        auth_plugin='mysql_native_password',
        database="site_db")
except Error as e:
    print(e)

def check_exist(username):
    query = f'SELECT username FROM site_db.users'
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        list_usernames = []
        for name in result:
            list_usernames.append(name[0])
        return username in list_usernames

def insert_one(dictionary_data: dict): #username: username
    values = list(dictionary_data.values())
    query = f'INSERT INTO users (username, phone_number, hashed_pass) VALUES (\'{values[0]}\', \'{values[1]}\', \'{values[2]}\')'
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        print('insertion user error')

def get_user_from_db(username):
    query = f'SELECT * FROM site_db.users WHERE users.username = \'{username}\''
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = tuple(cursor.fetchall())
        if not result:
            return False
        result = result[0]
        d = {
            'username': result[0],
            'phone_number': result[1],
            'hashed_pass': result[2]
        }
        return d
