from pymongo import MongoClient

MONGO_URI = "YOUR_MONGO_URL .."
conn = MongoClient(MONGO_URI)

# Test the connection
print("Connected to MongoDB:", conn.list_database_names())
