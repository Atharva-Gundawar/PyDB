from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Get a database
db = client['<DATABASE NAME>']

# List Database names
db_names = client.list_database_names()
print(db_names)

# Get the database named in the MongoDB connection URI.
client = MongoClient('mongodb://host/my_database')
db = client.get_default_database()

# Get a cursor over the databases of the connected server.
client.list_databases(session = None)

# Drop a database.
client.drop_database(name_or_database = 'my_database')