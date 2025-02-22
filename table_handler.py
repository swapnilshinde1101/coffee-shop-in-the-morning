import mysql.connector
from flask import Flask, request, render_template, redirect, url_for, flash

# Flask setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mydatabase"
}

def handle_booking_form(form_data):
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create the SQL query with parameterized statements for security
        query = """
            INSERT INTO tableorder (table_number, menu_items, quantity, customer_name, mobile_number, email, messages)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (form_data["table_number"], form_data["menu_items"], form_data["quantity"],
                  form_data["customer_name"], form_data["mobile_number"], form_data["email"], form_data["messages"])

        # Execute the query
        cursor.execute(query, values)
        conn.commit()

        return "Booking saved successfully!"

    except mysql.connector.Error as err:
        # Handle database connection or query execution errors
        return f"Error connecting to database: {err}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/book', methods=['GET', 'POST'])
def book_table():
    if request.method == 'POST':
        # Collect form data
        form_data = {
            "table_number": request.form.get("table_number"),
            "menu_items": request.form.get("menu_items"),
            "quantity": request.form.get("quantity"),
            "customer_name": request.form.get("customer_name"),
            "mobile_number": request.form.get("mobile_number"),
            "email": request.form.get("email"),
            "messages": request.form.get("messages")
        }

        # Call the function to insert the data into the database
        response_message = handle_booking_form(form_data)

        # Display the response (you can also redirect or render a page with this message)
        flash(response_message)  # Flask's flash for temporary messages
        return redirect(url_for('book_table'))

    return render_template('book_table.html')  # Render your form template (adjust path as needed)

if __name__ == '__main__':
    app.run(debug=True)
