# Install pymongo using 'pip install pymongo'

import urllib

from pymongo import MongoClient
client = MongoClient()

# Connect to localhost :
# Format :
# client = MongoClient('<host>', port_number)
client = MongoClient('localhost', 27017)
#  or use the entire URL
# client = MongoClient('mongodb://<host>:<portnum>/')
client = MongoClient('mongodb://localhost:27017/')

# Connect via URI :
# Use pip3 install pymongo[tls] for connecting to atlas
# Format :  
# client = pymongo.MongoClient(<Atlas connection string>)
client = MongoClient('mongodb+srv://admin:<password>@cluster0-pm5vp.mongodb.net/test?retryWrites=true&w=majority')

# Percent-Escaping Username and Password
username = "Atharva"
password = r"pass/with\alltpyes`of-chars"
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (urllib.parse.quote_plus(username), urllib.parse.quote_plus(password)))

# With encryption
# Here authSource overrides the default database name which is admin
# SCRAM-SHA-1/SCRAM-SHA-256
client = MongoClient('localhost',username='Atharva',password='password',authSource='some_db',authMechanism='SCRAM-SHA-256')

# TLS/SSL connections with certificate validation
# The MONGODB-X509 mechanism authenticates a username derived from the
# distinguished subject name of the X.509 certificate presented by the driver during TLS/SSL negotiation.
client = MongoClient('localhost',username="<X.509 derived username>",authMechanism="MONGODB-X509",tls=True,tlsCertificateKeyFile='/path/to/client.pem',tlsCAFile='/path/to/ca.pem')

# AWS Connections
# Authenticate using AWS IAM credentials
# The access_key_id and secret_access_key passed into the URI MUST be percent escaped.
client = MongoClient("mongodb://<access_key_id>:<secret_access_key>@localhost/?authMechanism=MONGODB-AWS")

# Check status
print(client.stats) 