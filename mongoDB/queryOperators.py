import datetime
from pymongo.collation import Collation
from pymongo import MongoClient
import re
import pymongo

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['<DATABASE NAME>']

# Get a collection from instance
collection = db.some_collection

# Some data
data = {'name': "Atharva Gundawar",
        'age': 100,
        'gender': "Male",
        'greetings': ['hello', 'hello again', 'hello once more']
        }

# Insert one data/document
insert_result = collection.insert_one(data)

# Confirm that insert is successful
print(insert_result.acknowledged)

# See the document ID
print(insert_result.inserted_id)

# Return a list of distinct values for the given key.
print(collection.distinct( "age" ))

# Shows all data of collection
print(list(collection.find()))

# Find the inserted document using the objectID
print(list(collection.find({'_id': insert_result.inserted_id})))

# find, can use one key or more
list(collection.find({'name': "Atharva Gundawar"}))

n = 5

# gets first n documents matching the given query
list(collection.find().limit(n))

# gets all documents skipping first n documents
list(collection.find().skip(n))

# Update an existing document
update_result = collection.update_one(
    {'name': "Atharva Gundawar"},
    {'$set': {'age': 50}}
)
# or
collection.find_one_and_update(
    {'name': "Atharva Gundawar"}, {'$set': {'age': 50}})

# Insert a new document with update, will avoid to crash during insert if document already exist
insert_result = collection.update_one(
    {'name': 'Atharva'}, {'$set': {'age': 50}}, upsert=True)

# show update results
print(update_result.raw_result)
print(update_result.acknowledged)

# Delete The first found document
delete = collection.delete_one({'name': 'Atharva'})

# Display deleted count
print(delete.deleted_count)

collection.insert_many([
    {
        'name': "Atharva Gundawar",
        'age': 100,
        'gender': "Male",
        'greetings': ['hello', 'hello again', 'hello once more'],
        'isActive': True,
    },

    {
        'name': "Manas Vardhan",
        'age': 100,
        'gender': "Male",
        'greetings': ['kaise ho', 'yo', 'heelo'],
        'isActive': True,
    },

    {
        'name': "Prannay Hebbar",
        'age': 100,
        'gender': "Male",
        'greetings': ['Hey', 'Heyy there', 'Namaste'],
        'isActive': True,
    }
])

print(collection.find(
    {'$or': [{'name': 'Prannay hebbar'}, {'name': 'Manas Vardhan'}]}))

# Update Multiple documents
collection.update_many({"$or": [{"age": 28}, {"age": 29}], "gender": 'Male'}, {
                       '$set': {'isActive': False}})

# Delete Multiple documents
# deletes as many documents as the filter
delete = collection.delete_many({'likes_python': True})

# Regex
# find documents which starts with Ath
regex = re.compile('^Ath', re.IGNORECASE)
print(collection.find({'name': regex}, {
      '_id': 0, 'name': 1, 'isActive': 1, 'age': 1}))

# Get ordered output
print(collection.find({'name': regex}, {'_id': 0, 'name': 1,
      'isActive': 1, 'age': 1}).sort('age', pymongo.ASCENDING))
# Use pymongo.DESCENDING for descending
# Use .limit(1) to get max/min