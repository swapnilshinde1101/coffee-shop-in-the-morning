<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mydatabase";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the required keys exist in the $_POST array
if (!isset($_POST['email']) || !isset($_POST['password'])) {
    echo "Error: Email and password are required.";
    exit;
}

$email = $_POST['email'];
$password = $_POST['password'];

// Validate email format
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "Error: Invalid email format.";
    exit;
}

// Hash the password before storing it
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Prepare SQL statement to prevent SQL injection
$stmt = $conn->prepare("INSERT INTO signin (email, password) VALUES (?, ?)");
$stmt->bind_param("ss", $email, $hashed_password); // "ss" means both parameters are strings

// Execute the query and check for success
if ($stmt->execute()) {
    echo "New user created successfully.";
} else {
    echo "Error: " . $stmt->error;
}

// Close the statement and connection
$stmt->close();
$conn->close();
?>
