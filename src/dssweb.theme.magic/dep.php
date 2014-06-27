<?php #!/usr/bin/env /usr/bin/php

error_reporting(E_ALL);
ini_set('display_errors', '1');
set_time_limit(0);

// Note: We're not getting json data in a $_REQUEST['payload'] parameter so using file_get_contents()
//echo "Post is: <pre>".print_r(file_get_contents('php://input'),true)."</pre>";

try {

  $payload = json_decode(stripslashes(file_get_contents('php://input')));
 
}
catch(Exception $e) {
 
    //log the error
    file_put_contents('/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/dss-plone-sandbox/logs/github.txt', $e . ' ' . $payload, FILE_APPEND);
    
    echo "<p>Error: $e</p>";

      exit(0);
}

if ($payload->ref === 'refs/heads/master') {

    $project_directory = '/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/';

    $output = shell_exec("/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/dep.sh");

    //log the request
    file_put_contents('/var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/dss-plone-sandbox/logs/github.txt', $output, FILE_APPEND);

    echo "<p>Success</p>";
}
?>
