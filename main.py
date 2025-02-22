import mysql.connector
from mysql.connector import Error

try:
    # Attempt to establish a connection
    conn = mysql.connector.connect(
        host='localhost',
        database='webpython',  # Ensure this is the correct database name
        user='root',            # Change this if your username is different
        password=''             # Use your actual password
    )

    if conn.is_connected():
        # Get server information
        db = conn.get_server_info()
        print("Connected to MySQL server", db)

        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Execute a query to fetch data from the 'login' table
        cursor.execute('SELECT * FROM login')

        # Fetch all records from the query result
        records = cursor.fetchall()

        if records:
            # Loop through the fetched records and print each row
            for result in records:
                print(result)
        else:
            print("No records found in the 'login' table.")

        # You can uncomment and modify the following lines to insert data into the table
        # email = "user@example.com"
        # password = "your_password"
        # cursor.execute("INSERT INTO login (email, password) VALUES (%s, %s)", (email, password))
        # conn.commit()  # Don't forget to commit the changes to save them to the database
        # print(f"Record inserted: {email}")

except Error as e:
    # Handle connection or query execution errors
    print("Error while connecting to MySQL", e)

finally:
    # Ensure the cursor and connection are closed properly
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
