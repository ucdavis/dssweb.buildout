<?php

// Use in the "Post-Receive URLs" section of your GitHub repo. Check.
 
if ( $_POST['payload'] ) {
shell_exec( 'cd /var/www/vhosts/cakefarm.com/subdomains/ucd/httpdocs/dss/wireframe-git/dss-plone-sandbox && git reset --hard HEAD && git pull' );
}