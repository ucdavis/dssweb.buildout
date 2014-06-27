<?php #!/usr/bin/env /usr/bin/php

error_reporting(E_ALL);
ini_set('display_errors', '1');
set_time_limit(0);
 
try {
 
  $payload = json_decode($_POST['payload']);
 
}
catch(Exception $e) {
 
    //log the error
    file_put_contents('/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/logs/github.txt', $e . ' ' . $payload, FILE_APPEND);
 
      exit(0);
}
 
if ($payload->ref === 'refs/heads/master') {
 
    $project_directory = '/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/';
 
    $output = shell_exec("/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/dep.sh");
 
    //log the request
    file_put_contents('/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/logs/github.txt', $output, FILE_APPEND);
 
}
?>