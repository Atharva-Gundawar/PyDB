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