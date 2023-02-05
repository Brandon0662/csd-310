from pymongo import MongoClient
 
url = "mongodb+srv://admin:admin@atlascluster.ztpyedf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

db = client.pytech

students = db.students

Tom = {
    "student_id": "1010",
    "first_name": "Tom",
    "last_name": "Ross",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 13, 2020",
            "end_date": "September 17, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B-"
                }
            ]
        }
    ]

} 

student_list = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

print("\n  -- INSERT STATEMENTS --")
Tom_student_id = students.insert_one(Tom).inserted_id
print("  Inserted student record Tom Ross into the students collection with document_id " + str(Tom_student_id))

Tom = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1010 --")
print("  Student ID: " + Tom["student_id"] + "\n  First Name: " + Tom["first_name"] + "\n  Last Name: " + Tom["last_name"] + "\n")

deleted_Tom = students.delete_one({"student_id": "1010"})

student_list = students.find({})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")


for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")