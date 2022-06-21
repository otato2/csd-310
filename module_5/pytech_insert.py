# Nicholas Werner 
# CSD 310 - Module 5.3 Assignment
# 06/14/2022
# add records to the students collection following instructors instructions

# setup code for access
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.hoqlh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students

# testing code to ensure only 1 set of records are present in the db
db.delete_many({})

print("-- INSERT STATEMENTS --")

# create the records
alpha = {"student_id": 1007, "first_name": "James", "last_name": "Camerson" }
beta = {"student_id": 1008, "first_name": "Jared", "last_name": "Puzo"  }
charlie = {"student_id": 1009, "first_name": "Shellie", "last_name": "Werner" }

# insert the records & display results
a_id = db.insert_one(alpha).inserted_id
print(f"Inserted student record {alpha['first_name']} {alpha['last_name']} into the students collection with document_id {a_id}")

b_id = db.insert_one(beta).inserted_id
print(f"Inserted student record {beta['first_name']} {beta['last_name']} into the students collection with document_id {b_id}")

c_id = db.insert_one(charlie).inserted_id
print(f"Inserted student record {charlie['first_name']} {charlie['last_name']} into the students collection with document_id {c_id}")