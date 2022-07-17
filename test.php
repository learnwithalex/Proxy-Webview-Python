<?php 

$command = escapeshellcmd('getwebpage.py');
$output = shell_exec($command);
echo $output;
