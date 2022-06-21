# Nicholas Werner
# CSD 310 - Module 6.2 Assignment
# 06/20/2022
# Following instructions, display students documents, update one record and display the updated record

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.hoqlh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students

# For testing, update original document with original last name; Camerson
#db.update_one( {"student_id": 1007}, {"$set": {"last_name": "Camerson"}})

# Display all documents using find
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Get list of documents
lst = db.find({})

# loop through the list of documents
for lt in lst:
    print(f"Student ID: {lt['student_id']}\nFirst Name: {lt['first_name']}\nLast Name: {lt['last_name']}\n")

# Update document using update_one
db.update_one( {"student_id": 1007}, {"$set": {"last_name": "Brooks"}})

# Display end result of update using find_one
print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")

# Get desired document and display it back
output = db.find_one({'student_id': 1007})
print(f"Student ID: {output['student_id']}\nFirst Name: {output['first_name']}\nLast Name: {output['last_name']}\n")
