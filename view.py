from .mysql_utils import create_connection, execute_query, execute_read_query, insert_order

def some_view(request):
    # Create connection
    connection = create_connection('localhost', 'root', 'customer')

    # Execute queries
    execute_query(connection, "CREATE TABLE IF NOT EXISTS coffee (id INT AUTO_INCREMENT PRIMARY KEY, table_number INT, menu_items VARCHAR(255), quantity INT, customer_name VARCHAR(255), mobile_number VARCHAR(255), email VARCHAR(255), message VARCHAR(255))")

    # Inserting an order
    insert_order(connection, 1, 'Latte', 2, 'John Doe', '1234567890', 'john@example.com', 'Extra hot')

    # Reading data
    orders = execute_read_query(connection, "SELECT * FROM coffee")

    # Close connection
    connection.close()

    return render(request, 'template.html', {'orders': orders})