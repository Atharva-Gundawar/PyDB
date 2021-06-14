from pymongo.collation import Collation
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['<DATABASE NAME>']

# Get a collection from instance
collection = db.some_collection

# Some data 
data = {  'name' : "Atharva Gundawar" , 
          'age' : 100,
          'gender' : "Male",
          'greetings': ['hello','hello again','hello once more'] # Array        
       }

#Insert one data/document
insert_result = collection.insert_one(data)

# Confirm that insert is successful
print(insert_result.acknowledged)

# See the document ID
print(insert_result.inserted_id)

# Shows all data of collection
print(list(collection.find()))

# Find the inserted document using the objectID
print(list(collection.find( {'_id' : insert_result.inserted_id })))  

# find, can use one key or more
list(collection.find( {'name' : "Atharva" }))                    

n = 5

# gets first n documents matching the given query
list(collection.find().limit(n))                             

# gets all documents skipping first n documents
list(collection.find().skip(n))                              

# Update an existing document
update_result = collection.update_one( 
    {'name' : "Atharva"}, 
    {'$set' : { 'age' : 50 }}
    ) 
# or
collection.find_one_and_update( {'name' : "Atharva"}, {'$set' : { 'age' : 50 }})

# Insert a new document with update, will avoid to crash during insert if document already exist
insert_result = collection.update_one( {'name' : 'Atharva'}, {'$set' : { 'age' : 50 }}, upsert= True)

# show update results
print(update_result.raw_result)
print(update_result.acknowledged)
