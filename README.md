# bloodpath

Aggressor script for Cobalt Strike to mark users as owned in BloodHound from the Cobalt Strike credentials tab. Speeds up the process.

'bloodpath.cna' calls for 'owned.py' from the working directory, so place both files in the root folder of your Cobalt Strike installation. (i.e. /opt/cobaltstrike/) make the 'owned.py' script executable (important!)

Cobalt Strike's Script Console will output the username node that it is marking in BloodHound.

Modify the 'dbusername' and 'dbpassword' variables in the owned.py script to apply to your neo4j bloodhound credentials.

If using a team bloodhound server, modify the 'url' variable in the owned.py script to point to the server.
