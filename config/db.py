from pymongo import MongoClient

MONGO_URI = "mongodb+srv://arifrahaman2606:NTambC6dzWTscSn1@mernstack.emb8nvx.mongodb.net/PDFS"
conn = MongoClient(MONGO_URI)

# Test the connection
print("Connected to MongoDB:", conn.list_database_names())
