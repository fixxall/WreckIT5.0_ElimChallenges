<?php
$images = [
    '1.png',
    '2.png',
    '3.png',
    '4.png',
    '5.png'
];

if (isset($_GET['url'])) {
    $url = $_GET['url'];

    $curl = curl_init();

    curl_setopt($curl, CURLOPT_URL, $url);  
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);  
    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);  
    curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, 10);  
    curl_setopt($curl, CURLOPT_TIMEOUT, 30);  

    $content = curl_exec($curl);

    if ($content === false) {
        echo "Error fetching content: " . curl_error($curl);
    } else {
        echo $content;
    }

    curl_close($curl);

    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>cheems</title>
    <style>
        img {
            margin: 10px;
            width: 200px;
            height: 200px;
            object-fit: cover;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>cheems hold the flag</h1>
    <div>
        <?php foreach ($images as $image): ?>
            <a href="?image=<?php echo urlencode($image); ?>">
                <img src="img/<?php echo htmlspecialchars($image); ?>" alt="flag">
            </a>
        <?php endforeach; ?>
    </div>
</body>
</html>
