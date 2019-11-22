# bloodpath
Agressor script for Cobalt Strike to mark users as owned in bloodhound from the Cobalt Strike credentials tab.

bloodpath.cna calls for owned_utils.py from the working directory, so place both files in the root folder of your Cobalt Strike installation

Cobalt Strike's Script Console will output the username node that it is marking in BloodHound.

Modify the 'dbusername' and 'dbpassword' variables in the owned_utils.py script to apply to your neo4j bloodhound credentials.
If using a team bloodhound server, modifying the 'url' variable in the owned_utils.py script to point to the server.
