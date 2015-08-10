Developing using dssweb.buildout
================================

When developing:

    python2.7 ./bootstrap.py -c development.cfg
    bin/buildout -c development.cfg
    bin/supervisord
    bin/client1 fg

The supervisor controls only the zeoserver by default.

Updating the theme (this happens automatically when running buildout):

    bin/compass compile -c src/dssweb.theme.magic/config.rb --app-dir src/dssweb.theme.magic


OpsWorks Overview
-----------------

Deployments are done via AWS OpsWorks.  The current default stack is called
`DSS Stack` and resides in the `us-west-1` (Oregon) region.  All configuration
for the servers should be done via the OpsWorks web console.  Configuration
changes made via SSH or the EC2 console are likely to be overwritten or lost.

A few important concepts from OpsWorks:

* Stack: a container for application and server configuration

* Layer: a set of recipes and dependencies to be run on a server throughout
its lifecycle

* Instance: a description of a server (not the same as an EC2 instance), can
be assigned multiple Layers of functionality, and started and stopped.
Instance store instances are destroyed when stopped and created when started,
EBS instances have persistent storage which is retained across stops and
starts.

* Application: a description of an application, including its code
repositories, credentials, and database connections.

* Recipe: a set of resources to be created/managed and commands to run,
defined using the Chef configuration management system.


There are some specific stages of the instance lifecycle which trigger recipes
to be run:

* Setup: The first set of recipes run after an instance boots.  These install
dependencies and setup services.

* Configure: Recipes run automatically on all instances whenever a new
instance is added or removed from the stack.

* Deploy: Recipes run when an application is deployed (code is checked out
and installed)

* Shutdown: Recipes run when in an instance is stopped.


The setup and configure stages can be triggered manually at any time using the
`Run Command` button from the `Stack` or `Deployments` panels.  Applications
can be deployed from the `App` or `Deployments` panels.  Specific recipes can
also be run manually using the `Run Command` button.  Similarly, you can
install the dependencies for layers, or update all packages or even the OS
(not recommended) using the `Run Command` button.  The default stack
configuration automatically updates OS packages nightly.


Deploying Code Changes
----------------------

To deploy code changes, navigate to the `Deployments` section of the OpsWorks
console for the stack, click the `Deploy an App` button and deploy the `Plone
Instances` app. This will create a fresh clone of the buildout from Github,
and if the configuration has changed, re-run buildout and restart the
instances (with an optional rolling delay) on all selected servers.


Configuring the Deployment
--------------------------

The deployment is configured from the `Stack` panel in the OpsWorks console
using the `Stack Settings` button.  From there you can see and edit the JSON
configuration for the stack.  For details on specific settings see the
[opsworks plone buildout documentation](https://github.com/alecpm/opsworks-web-python/tree/master/plone_buildout).


### Adding a hostname mapping for a sub-site

To add a new hostname mapping to a specific subsite, simply update the
`plone_instances[subsites]` mapping in the Custom JSON.  For example:

    ...
    "subsites": {".mycustomdomain.ucdavis.edu": "customdomain_path"}
    ...

That configuration would add a virtual host for *.mycustomdomain.ucdavis.edu
to the site path `/Plone/customdomain_path`.  Once that change is made you can
use the `Run Command` button from either the Stack or Deployments panel, to
initiate a `Configure` on all of the servers in the HAProxy layer (which
manages the front end configuration).


### Adding additonal nginx configuration for a subsite

There is another mapping in the Custom JSON `subsite_config`, which allows you
to set further custom nginx configuration declarations for a given subsite.
You can set things like the following:

    ...
    "subsite_config": {".mycustomdomain.ucdavis.edu": "\nif ($host ~ '^mycustomdomain.ucdavis.edu$') {\n  rewrite ^(.*)$ http://www.mycustomdomain.ucdavis.edu$1 permanent;\n  break;\n}\n"}
    ...

Which will redirect all requests to `mycustomdomain.ucdavis.edu` to
corresponding urls on `www.mycustomdomain.ucdavis.edu`.  Once again, you would
use the `Configure` action to update the nginx configuration and reload the
server.

If including configuration directly in the Custom JSON is not desirable, you
can include more complex nginx configuration files which live in the buildout:

   ...
    "subsite_config": {".mycustomdomain.ucdavis.edu": "\ninclude /srv/www/plone_instances/current/src/mycustomdomain_config/config\n"}
    ...

Here we reference a file included in the `src/` directory by mr.developer,
which allows us to pull updates without forcing a deploy.  When the included
file is updated, you would need to run an update using
`Stack -> Run Command -> Execute Recipes`.  Enter
`plone_buildout::instances-develop-up, plone_buildout::nginx`, then under `Advanced`
enter `{"nginx_plone": {"force_reload": true}}` into the `Custom Chef JSON`
and select the servers in the HAProxy layer before exceuting the recipes.  This will
update the repositories in `src/` and then update the nginx configuration.


### Adding custom nginx configuration for the default site

Similar to the subsite configuration above, you can set custom nginx
configuration using the `nginx_plone["additional_config"]` attribute of the
Custom JSON.  The nginx server can be updated and reloaded as described above.


Adding Additional Plone Servers
-------------------------------

### Adding a full time server running additional plone instances

From the Instances panel, click the `+ Instance` button under the `Plone
Instances` layer.  This will allow you to add a new server to run Plone
clients.  Choose an instance size, availability zone, optionally an SSH key,
and select `24/7` under `Advanced -> Scaling type`.  I recommend choosing
`Instance store` for a full time instance, for lower costs and better
performing disk caches.  Click `Add Instance`, and then `start` the new
instance.  After a short while, a new instance should be up and running with
an appropriate number of Plone clients automatically registered with the load
balancer.


### Adding a time based instance

If you have predictable periods of high load and would like to run additional
servers during those periods, you can use `Time-based instances`.  Follow the
steps above for adding a full time instance, but select `Time-based` under
`Advanced -> Scaling type`.  Now you can click the instance name, and follow
the link under `Time-based (configuration)` to set the times and days of the
week during which the instance will run (all times are set in UTC).  You will
only be charged for these instances when they are running.


### Adding a load based instance

If you want to automatically create a new set of Plone instances when the
server load reaches certain thresholds, you can use `Load-based instances`.
Follow the instructions above, but select `Load-based` under `Advanced ->
Scaling type`.  For load-based instances I recommend using EBS backed
instances with SSD storage, in order to ensure faster instance creation during
periods of high load.  Now you can click the instance name, and follow the
link under `Load-based (configuration)`.  There you can enable the instance
and set thresholds for stopping and starting instances based on CPU, RAM, or
Load usage.

You can also use the sub-panels under `Instances` to manage load-based and
time-based instances.


Spreading the Stack Across Availability Zones
---------------------------------------------

If you wish to have a high-availability stack, you will want to have servers
with all layers (except `DB Packing`) in multiple Availability Zones.  You may
wish to have two servers with all layers assigned, or two smaller servers
assigned to e.g. `HAProxy` and `Memcached` layers, and additional larger
servers assigned to `Plone Instances`.  The `DB Packing` layer should only be
run on a single server assigned to the `Plone Instances` layer, regardless of
your instances' configuration.  The RDS database should also be setup for
`Multi- AZ` operation, as it is by default for production use.

By default the production stack is setup with an `Elastic Load Balancer` layer
which is assigned to the HAProxy layer, and routes traffic among servers in
that layer.


Cloning the Stack
-----------------

The first step (because it takes a little time to complete) is to clone the
database. Navigate to the RDS console in the appropriate region, select the
desired RDS instance and use the `Instance Actions` menu to `Take Snapshot`.
Choose a snapshot name and click `Take Snapshot`.  You should see your named
snapshot in the list under the `Snapshots` section, and when the snapshot is
completed, you can select it and click `Restore Snapshot`.  This will allow
you to create a new RDS instance from the snapshot.  You should need only to
give it a unique identifier and select whether or not it will be Multi-AZ
before clicking "Restore DB Instance".  If you want to clone and RDS to
another region, you will first need to "Copy Snapshot" into that region before
restoring it.

If you want to create additional server stacks with their own databases (e.g.
for staging or development), you can use the stack cloning feature.  Navigate
to the OpsWorks Dashboard, and use the `Actions` menu next to the desired
stack and choose `clone`.  By default all attributes of the stack except for
the instances and DB assignments will be cloned, but you can make
modifications to the settings, including the region in which the cloned stack
will be located.

You'll need to add an RDS layer for your new RDS database.  Navigate to the
Layers panel and click `+ Layer` at the bottom of the screen.  Choose the
`RDS` tab, select your newly created RDS instance, set the `User` (usually
`root`), and `Password` for the DB (these can be reset in the RDS console for
the DB instance), and click `Register with Stack` (this will only work once
the RDS clone is complete and in the `available` state).

You will then need to edit the `Plone Instance` App from the `Apps` panel, and
set the `Data source type` to `RDS`, the `Database instance` to your newly
registered RDS server, and `Database name` to the same value it had in the App
in the original stack (probably `plone_rds_primary`).

Once that's done, you can assign instances to the layers. Under the
`Instances` panel, you can add a new instance to a layer (as described above),
and then in later layers, you can choose to add an `Existing OpsWorks`
instance to add the instance to additional layers.  Once your instances are
assigned to all the desired layers, you can start them.

Once you have e.g. a staging stack setup, you should be able to add new RDS
layers for newly cloned RDS database in order to update the data. You'll just
need to update the database section in the `App`run a `Configure` command on
the stack to deploy the configuration changes.


Upgrading the Database
----------------------

The initial RDS DB has 200 GB of allocated storage, but is easily upgradeable.
From the RDS console, you can select the RDS instance and choose `Instance
Actions -> Modify` to modify the parameters of the DB.  From there you can
upgrade the DB instance class (CPU and RAM), and the allocated storage size
and type (I do not recommend changing the storage type for General Purpose
SSD).  Additionally, you can update the password, backup settings, and DB
parameters.  Unless there is an urgent need to upgrade immediately, it is best
to allow the modifications to occur during the weekly maintenance window.  If
the modifications are needed urgently, then you can check the `Apply
Immediately` box to apply the changes immediately, which may result in some
performance degradation, depending on the actions being taken.


Upgrading (or Downgrading) the Servers
--------------------------------------

I recommend performing rolling server upgrades.  You can create a new instance
and assign it to all the layers of the instance it is intended to replace, and
start it.  Once it is available, you can stop the older instance.

If donwtime isn't a problem, you can simply stop the instance, edit it to
change the instance type, and then start it again.  There will be some
limitations on instance type, based on the originally selected instance type
(e.g. whether it is EBS or instance store backed)
