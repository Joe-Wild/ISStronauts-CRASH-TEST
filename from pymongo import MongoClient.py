# This is the access of the "Connecting MongoDB Driver" 
# 2 Versions exist for Programming Users and Non_Programming Users



from pymongo.mongo_client import MongoClient

uri = "mongorestore --uri mongodb+srv://joewildtoybox:<WbGeAQOlWhTPGtU9>@jwdb.zfw3yct.mongodb.net"
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)











