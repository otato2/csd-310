# Nicholas Werner
# CSD 310 - Module 6.3 Assignment
# 06/20/2022
# description

from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.hoqlh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students

# Created method for displaying list of student documents
def display_list():
    results = db.find({})
    for single in results:
        print(f"Student ID: {single['student_id']}\nFirst Name: {single['first_name']}\nLast Name: {single['last_name']}\n")

# Display all documents using find
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

display_list()

# Use insert_one to add document for student 1010
print("-- INSERT STATEMENTS --")

record = {"student_id": 1010, "first_name": "Natasha", "last_name": "Johnson" };
output = db.insert_one(record).inserted_id
print(f"Inserted student record {record['first_name']} {record['last_name']} into the students collection with document_id {output}\n")

# Display all documents again using find
print("-- DISPLAYING NEW STUDENT LIST DOC --")

display_list()

# Delete document for student 1010 then display all documents again with document removed

db.delete_one({"student_id": 1010})

print("-- DELETED STUDENT ID: 1010 --")

display_list()

