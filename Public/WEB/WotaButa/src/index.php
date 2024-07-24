<?php
// Disable error reporting
error_reporting(0);

// Check for underscores in the query string and terminate if found
if (preg_match("/\_/i", $_SERVER["QUERY_STRING"])) {
    exit();
}

// Include the database connection file
include "conn.php";

// Establish a connection to the database
$connection = mysqli_connect($host, $dbuser, $dbpass);

// Check if the connection was successful
if (!$connection) {
    echo "Connection to MySQL failed: " . mysqli_error();
}

// Select the database
mysqli_select_db($connection, $dbname) or die("Unable to select database: $dbname");

// Loop through each GET parameter
foreach ($_GET as $key => $value) {
    $query = "SELECT * FROM words WHERE id=('$key') LIMIT 0,1";
    echo $query . "\n";
    $result = mysqli_query($connection, $query);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blind Wota :)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .bg-pink-custom { background-color: #FFC0CB; }
        .text-pink-custom { color: #FFC0CB; }
        .border-pink-custom { border-color: #FFC0CB; }
    </style>
</head>
<body class="bg-pink-custom">
    <h1 class="text-3xl text-center mt-5 text-white">Ayo Adu Argumen?</h1>
    <div class="overflow-x-auto relative shadow-md sm:rounded-lg m-10">
        <table class="w-full text-sm text-left text-gray-700">
            <thead class="text-xs uppercase bg-white text-gray-700">
                <tr>
                    <th scope="col" class="py-3 px-6 text-center border-b border-pink-custom">Query</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($_GET as $key => $value) : ?>
                    <tr class="bg-white border-b border-pink-custom hover:bg-pink-100 text-center">
                        <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap">
                            <pre>SELECT * FROM words WHERE id=('<?= $key; ?>') LIMIT 0,1</pre>
                        </th>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>
</html>

