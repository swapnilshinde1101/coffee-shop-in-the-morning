<?php
// Connect to the database
$host = 'localhost';
$username = 'root';
$password = ''; // Enter your actual password here
$database = 'webpython';

$conn = mysqli_connect($host, $username, $password, $database);

// Check for connection errors
if (mysqli_connect_errno()) {
    die('Failed to connect to the database: ' . mysqli_connect_error());
}

// Handle form submission
if (isset($_POST['table_number']) && isset($_POST['menu_items']) && isset($_POST['quantity']) && isset($_POST['customer_name']) && isset($_POST['mobile_number']) && isset($_POST['email']) && isset($_POST['message'])) {
    $table_number = mysqli_real_escape_string($conn, $_POST['table_number']);
    $menu_items = mysqli_real_escape_string($conn, $_POST['menu_items']);
    $quantity = mysqli_real_escape_string($conn, $_POST['quantity']);
    $customer_name = mysqli_real_escape_string($conn, $_POST['customer_name']);
    $mobile_number = mysqli_real_escape_string($conn, $_POST['mobile_number']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $message = mysqli_real_escape_string($conn, $_POST['message']);

    // Insert data into the database
    $query = "INSERT INTO orders (table_number, menu_items, quantity, customer_name, mobile_number, email, message) 
              VALUES ('$table_number', '$menu_items', '$quantity', '$customer_name', '$mobile_number', '$email', '$message')";

    if (mysqli_query($conn, $query)) {
        echo "<p>Data inserted successfully!</p>";
    } else {
        echo "<p>Failed to insert data: " . mysqli_error($conn) . "</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About</title>

  <link rel="stylesheet" href="https://unpkg.com/swiper@7/swiper-bundle.min.css" />
  <link rel="stylesheet" href="style.css" />
  <link rel="shortcut icon" href="image/favicon.ico" type="image/x-icon">
</head>

<body>
  <header class="header">
    <div id="menu-btn" class="fas fa-bars"></div>
    <a href="#" class="logo">coffee <i class="fas fa-mug-hot"></i></a>
    <nav class="navbar">
      <a href="index.html">home</a>
      <a href="about.html">about</a>
      <a href="menu.html">menu</a>
      <a href="review.html">review</a>
      <a href="book.html">book Table</a>
      <a href="footer.html">Contact us</a>
    </nav>
    <div>
      <a class="btn" onclick="openForm()">Sign In</a>
      <a class="btn">Sign Up</a>
    </div>
    <div class="form-popup" id="myForm">
      <form action="login.py" method="post" class="form-container">
        <h1>Login</h1>
        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" name="email" id="eml" required>
        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" name="password" id="pwd" required>
        <button type="button" class="btn" onclick="auth()">Login</button>
        <button type="button" class="btn cancel" onclick="closeForm()">Close</button>
      </form>
    </div>

    <script>
      function auth() {
        var email = document.getElementById("eml").value;
        var password = document.getElementById("pwd").value;
        if (email == "coffee@gmail.com" && password == "123123") {
          window.location.assign("book.html");
          alert("Login Successfully!");
        } else {
          alert("Please Enter Valid Data");
        }
      }

      function openForm() {
        document.getElementById("myForm").style.display = "block";
      }

      function closeForm() {
        document.getElementById("myForm").style.display = "none";
      }
    </script>
  </header>

  <!-- BOOK -->
  <section class="book" id="book">
    <h1 class="heading">Booking <span>Reserve a Table</span></h1>
    <form action="" method="post">
      <input type="number" placeholder="Table Number" name="table_number" class="box" required />
      <input type="text" placeholder="Menu" name="menu_items" class="box" required />
      <input type="number" placeholder="Quantity" name="quantity" class="box" required />
      <input type="text" placeholder="Customer Name" name="customer_name" class="box" required />
      <input type="number" placeholder="Mobile Number" name="mobile_number" class="box" required />
      <input type="email" placeholder="Email" name="email" class="box" required />
      <textarea name="messages" placeholder="Message" class="box" id="" cols="30" rows="5"></textarea>
      <button type="submit" class="btn">Submit</button>
    </form>
  </section>

  <!-- SWIPER -->
  <script src="https://unpkg.com/swiper@7/swiper-bundle.min.js"></script>
  <script src="js/script.js"></script>
</body>
</html>
