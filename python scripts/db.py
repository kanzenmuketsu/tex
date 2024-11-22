import local_settings
from mysql.connector import connect, Error

db_host = local_settings.DBHOST
db_user = local_settings.DBUSER
db_pass = local_settings.DBPASS
db_name = local_settings.DBNAME

connection = None
def connect_db():
    try:
        global connection
        connection = connect(

        host=db_host,

        user=db_user,

        password=db_pass,

        auth_plugin='mysql_native_password',

        database=db_name)

        print("database connected")
    except Error as e:
        print(e)
connect_db()
def check_exist(username):
    connect_db()
    query = f'SELECT username FROM {db_name}.users'
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        list_usernames = []
        for name in result:
            list_usernames.append(name[0])
        return username in list_usernames

def insert_one(dictionary_data: dict): #username: username
    connect_db()
    values = list(dictionary_data.values())
    query = f'INSERT INTO users (username, email, hashed_password) VALUES (\'{values[0]}\', \'{values[1]}\', \'{values[2]}\')'
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except Error as e:
        print('insertion user error', e)

def get_product_from_db_by_name(page_name):
    connect_db()
    page_name = page_name.split('.')[0].replace('-', ' ')
    print(page_name,'#######')
    query = f'SELECT * FROM {db_name}.products WHERE products.short_info = \'{page_name}\''
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return list(result[0])

def get_user_from_db(username):
    connect_db()
    query = f'SELECT * FROM {db_name}.users WHERE users.username = \'{username}\''
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

def get_products_from_db(product_number: int) -> tuple:
    connect_db()
    # db_structure ['id', 'name', 'info', 'price', 'old_price', 'img1', 'img2', 'img3', 'amount'].

    query = f'SELECT * FROM {db_name}.products'
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

    return result[product_number-1]