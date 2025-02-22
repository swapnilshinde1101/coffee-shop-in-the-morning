import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                   database='webpython',
                                   user='root',
                                   password='')
    if conn.is_connected():
        db = conn.get_server_info()
        print("Connected to mysql server", db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM table_order')
        record = cursor.fetchall()
        for result in record:
            print(result)

except Error as e:
    print("Error while connecting ot database", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()


