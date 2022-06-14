# Nicholas Werner 
# CSD 310 - Module 5.3 Assignment
# 06/14/2022
# find records within the students collection using instructor instructions

# setup code for access
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.hoqlh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students

# find query & display results
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

lss = db.find({})

for ls in lss:
    print(f"Student ID: {ls['student_id']}\nFirst Name: {ls['first_name']}\nLast Name: {ls['last_name']}\n")

# find_one query & display results
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

a = db.find_one({'student_id': 1007})
print(f"Student ID: {a['student_id']}\nFirst Name: {a['first_name']}\nLast Name: {a['last_name']}\n")

