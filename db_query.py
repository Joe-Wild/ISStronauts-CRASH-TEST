from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if needed

# Access a specific database
db = client['mydatabase']  # Replace 'mydatabase' with your database name

# Access a specific collection
collection = db['mycollection']  # Replace 'mycollection' with your collection name


# Retrieve all documents from the collection
documents = collection.find()

# Iterate over the documents and print them
for document in documents:
    print(document)


 # Query documents with a specific condition
query = {'name': 'John Doe'}  # Replace with your query condition
documents = collection.find(query)

for document in documents:
    print(document)

 client.close()    