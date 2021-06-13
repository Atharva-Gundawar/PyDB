from pymongo.collation import Collation
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['<DATABASE NAME>']

# Get a collection from name
collection = db['<COLLECTION_NAME>']

# Get a collection from instance
collection = db.some_collection

# List collection names
collection_names = client.list_collection_names()

# Create a new collection
# create a new collection called contacts and assign a default collation with the fr_CA locale
collection = db.create_collection('contacts',collation=Collation(locale='fr_CA'))

# Delete collection
db.drop_collection('addressbook')