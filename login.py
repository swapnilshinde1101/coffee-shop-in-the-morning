import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a random secret key for your session

# Function to connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this to your MySQL username
            password='',  # Change this to your MySQL password
            database='webpython'  # Change this to your database name
        )
        print("Connected to database successfully!")
        return connection
    except mysql.connector.Error as err:
        print("Error: ", err)

# Route for displaying login page
@app.route('/')
def login_page():
    return render_template('index.html')

# Route for handling login form submission
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Connect to the database
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM login WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user[1], password):  # Check if the password is correct
            session['user'] = user[0]  # Store user info in session
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or admin page
        else:
            flash("Invalid email or password.", "error")
            return redirect(url_for('login_page'))  # Redirect back to login page
    
    flash("Database connection error.", "error")
    return redirect(url_for('login_page'))  # Redirect back to login page

# Route for admin dashboard (only accessible if logged in)
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash("You must log in first.", "error")
        return redirect(url_for('login_page'))
    return "Welcome to the admin dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
