# Nicholas Werner
# CSD 310 - Module 5.2 Assignment
# 06/14/2022
# print a list of collection names after setting up mongoDB & VSCode

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.hoqlh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())