<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Finder</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Page Finder</h1>
        <?php
        if (isset($_GET['page'])) {
            $page = $_GET['page'];
            include($page);
        } else {
            echo "<p>No page specified.</p>";
        }
        ?>
    </div>
</body>
</html>
