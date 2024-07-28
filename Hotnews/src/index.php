<?php
session_start();

// Dummy user data for demonstration purposes
$valid_username = "dummy";
$valid_password = bin2hex(random_bytes(128));;

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Check if the credentials are valid
    if ($username === $valid_username && strcmp($password,$valid_password)) {
        // Set session variables
        $_SESSION['username'] = $username;
        header("Location: main.php");
        exit();
    } else {
        $error = "Invalid username or password";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <?php
        if (isset($error)) {
            echo "<p style='color: red;'>$error</p>";
        }
        ?>
        <form action="login.php" method="post">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
