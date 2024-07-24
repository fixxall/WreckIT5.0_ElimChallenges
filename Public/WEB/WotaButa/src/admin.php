<?php
session_start(); // Start the session

$error = '';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $password = $_POST['password'];
    // Hardcoded password for demonstration purposes
    $correct_password = 'indiraoshikusatus4tunya';
    if ($password === $correct_password) {
        // Set session variable
        $_SESSION['loggedin'] = true;
        // Redirect to admin page or perform other actions
        header("Location: 3af3b3221714103a593acc24ae213767.php");
        exit();
    } else {
        $error = 'Password salah!';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login - JKT48 Style</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            background-image: url('https://thumb.viva.id/intipseleb/1265x711/2023/08/30/64eed1f229f4f-indira-jkt48.jpg');
            background-size: cover;
            background-position: center;
        }
    </style>
</head>
<body class="dark dark:bg-gray-900 bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-lg dark:bg-gray-800 bg-opacity-90 backdrop-filter backdrop-blur-md">
        <h2 class="text-3xl font-bold mb-4 text-gray-800 dark:text-white text-center">JKT48 Admin Login</h2>
        <?php if (!empty($error)) : ?>
            <p class="text-red-500 mb-4"><?php echo $error; ?></p>
        <?php endif; ?>
        <form action="" method="POST">
            <div class="mb-4">
                <label for="password" class="block text-gray-700 dark:text-gray-300">Masukkan Password</label>
                <input type="password" name="password" id="password" class="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-pink-500">
            </div>
            <button type="submit" class="w-full bg-pink-500 text-white px-3 py-2 rounded-md hover:bg-pink-600">Login</button>
        </form>
    </div>
</body>
</html>
