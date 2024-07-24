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
        :root {
            --pink-custom: #FFC0CB;
            --white: #FFFFFF;
            --gray-light: #F7FAFC;
            --gray: #E2E8F0;
            --gray-dark: #2D3748;
            --text-gray: #4A5568;
        }

        body {
            background-color: var(--pink-custom);
            font-family: 'Arial', sans-serif;
        }

        header {
            background-color: var(--white);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            padding: 1rem 0;
        }

        header h1 {
            color: var(--pink-custom);
        }

        header nav ul {
            display: flex;
            list-style: none;
        }

        header nav ul li a {
            color: var(--text-gray);
            margin-left: 1rem;
            text-decoration: none;
            transition: color 0.3s;
        }

        header nav ul li a:hover {
            color: var(--pink-custom);
        }

        h1, h2, h3 {
            color: var(--white);
            text-align: center;
        }

        h1 {
            margin-top: 2rem;
        }

        section {
            margin-top: 4rem;
            padding: 1rem;
        }

        section#news article,
        section#members .member-card,
        section#gallery .gallery-img {
            background-color: var(--white);
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            padding: 1rem;
            text-align: center;
            transition: transform 0.3s;
        }

        section#news article:hover,
        section#members .member-card:hover,
        section#gallery .gallery-img:hover {
            transform: translateY(-5px);
        }

        section#news article h3,
        section#members .member-card h3 {
            color: var(--text-gray);
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        section#news article p,
        section#members .member-card p {
            color: var(--text-gray);
        }

        section#gallery .gallery-img img {
            border-radius: 0.5rem;
            max-width: 100%;
            transition: transform 0.3s;
        }

        section#gallery .gallery-img img:hover {
            transform: scale(1.05);
        }

        footer {
            background-color: var(--white);
            box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.1);
            padding: 1.5rem 0;
            text-align: center;
        }

        footer p {
            color: var(--text-gray);
        }
    </style>
</head>
<body class="bg-pink-custom">
    <!-- Header -->
    <header class="bg-white shadow-md py-4">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold text-pink-custom">Blind Wota :)</h1>
            <nav>
                <ul class="flex space-x-4">
                    <li><a href="#" class="text-gray-700 hover:text-pink-custom">Home</a></li>
                    <li><a href="#news" class="text-gray-700 hover:text-pink-custom">News</a></li>
                    <li><a href="admin.php" class="text-gray-700 hover:text-pink-custom">Admin</a></li>
                    <li><a href="#members" class="text-gray-700 hover:text-pink-custom">Members</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto mt-10">
        <!-- Existing Function -->
        <section>
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
        </section>

        <!-- News Section -->
        <section id="news" class="mt-20">
            <h2 class="text-3xl text-center text-white">Latest News</h2>
            <div class="mt-10">
                <article class="bg-white p-6 rounded-lg shadow-md mb-6">
                    <h3 class="text-2xl font-bold text-gray-700">News Title 1</h3>
                    <p class="text-gray-700 mt-2">Masih dalam pengembangan...</p>
                </article>
                <article class="bg-white p-6 rounded-lg shadow-md mb-6">
                    <h3 class="text-2xl font-bold text-gray-700">News Title 2</h3>
                    <p class="text-gray-700 mt-2">Masih dalam pengembangan...</p>
                </article>
            </div>
        </section>

        <!-- Gallery Section -->
        <section id="gallery" class="mt-20">
            <h2 class="text-3xl text-center text-white">Gallery</h2>
            <div class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="gallery-img">
                    <img src="https://via.placeholder.com/300" alt="Gallery Image 1" class="w-full h-auto rounded-lg shadow-md">
                </div>
                <div class="gallery-img">
                    <img src="https://via.placeholder.com/300" alt="Gallery Image 2" class="w-full h-auto rounded-lg shadow-md">
                </div>
                <div class="gallery-img">
                    <img src="https://via.placeholder.com/300" alt="Gallery Image 3" class="w-full h-auto rounded-lg shadow-md">
                </div>
            </div>
        </section>

        <!-- Members Section -->
        <section id="members" class="mt-20">
            <h2 class="text-3xl text-center text-white">Members</h2>
            <div class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="member-card">
                    <img src="https://static.wikia.nocookie.net/akb48/images/5/5e/Shania_Gracia_JKT48_2024.jpg/revision/latest?cb=20240301082925" alt="Member 1" class="w-32 h-32 mx-auto rounded-full">
                    <h3 class="mt-4 text-2xl font-bold text-gray-700">Shania Gracia</h3>
                    <p class="text-gray-700">Captain</p>
                </div>
                <div class="member-card">
                    <img src="https://static.wikia.nocookie.net/akb48/images/7/79/Freya_Jayawardana_JKT48_2024.jpg/revision/latest?cb=20240301082927" alt="Member 2" class="w-32 h-32 mx-auto rounded-full">
                    <h3 class="mt-4 text-2xl font-bold text-gray-700">Freya Jayawardana</h3>
                    <p class="text-gray-700">Ace</p>
                </div>
                <div class="member-card">
                    <img src="https://static.wikia.nocookie.net/akb48/images/d/d2/Indira_Seruni_JKT48_2024.jpg/revision/latest?cb=20240301082927" alt="Member 3" class="w-32 h-32 mx-auto rounded-full">
                    <h3 class="mt-4 text-2xl font-bold text-gray-700">Indira Putri Seruni</h3>
                    <p class="text-gray-700">Member</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-white shadow-md py-6 mt-20">
        <div class="container mx-auto text-center text-gray-700">
            <p>&copy; 2024 Blind Wota :) All rights reserved.</p>
        </div>
    </footer>
</body>
</html>

