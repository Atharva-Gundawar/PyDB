from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Get a database from name
db = client['<DATABASE_NAME>']

# Get a database from instance
db = client.some_db

# List Database names
db_names = client.list_database_names()
print(db_names)

# Get the database named in the MongoDB connection URI.
client = MongoClient('mongodb://host/<DATABASE_NAME>')
db = client.get_default_database()

# Get a cursor over the databases of the connected server.
client.list_databases(session = None)

# Drop a database.
client.drop_database(name_or_database = '<DATABASE_NAME>')