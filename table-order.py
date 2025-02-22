import mysql.connector
from mysql.connector import Error

def create_connection(localhost, root, webpython):
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='customer',
            port ='3306'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_order(connection, table_number, menu_items, quantity, customer_name, mobile_number, email, message):
    query = """
    INSERT INTO coffee (table_number, menu_items, quantity, customer_name, mobile_number, email, message)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (table_number, menu_items, quantity, customer_name, mobile_number, email, message)
    execute_query(connection, query, values)