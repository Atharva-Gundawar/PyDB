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
          'randomList': ['hello','hello again','hello once more'] # Array        
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

# gets a Limited set of documents
list(collection.find().limit(1))                             

# gets all documents skipping first
list(collection.find().skip(1))                              

