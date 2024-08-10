<?php
session_start();
echo "<h2>Apakah ada ingpo minnn? no ingpokahh??? hmmm.....</h2>";

$num=$_GET['num'];
$page=$_GET['page'];

if(preg_match("/^[0-9+-\/\*e ]/i", $num)){
    exit("<h2>ga boleh angka<h2>");
}

if(preg_match("/flag|\.|php|conf|\*|'|\"/i", $page)){
    exit("<h2>hmmm jangan ya dek</h2>");
}


if(is_numeric($num)){
    if($page==null){
        echo phpinfo();
    }else{
        include_once($page);
    }
}else{
    highlight_file(__FILE__);
}

?>
