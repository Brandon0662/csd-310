from pymongo import MongoClient

url = "mongodb+srv://admin:admin@atlascluster.ztpyedf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

Bobby = {
    "student_id": "1007",
    "first_name": "Bobby",
    "last_name": "Johnson",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                }
            ]
        }
    ]

}

Jeff = {
    "student_id": "1008",
    "first_name": "Jeff",
    "last_name": "Thompson",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A-"
                }
            ]
        }
    ]
}

Brooke = {
    "student_id": "1009",
    "first_name": "Brooke",
    "last_name": "Davidson",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}

students = db.students

print("\n  -- INSERT STATEMENTS --")
Bobby_student_id = students.insert_one(Bobby).inserted_id
print("  Inserted student record Bobby Johnson into the students collection with document_id " + str(Bobby_student_id))

Jeff_student_id = students.insert_one(Jeff).inserted_id
print("  Inserted student record Jeff Thompson into the students collection with document_id " + str(Jeff_student_id))

Brooke_student_id = students.insert_one(Brooke).inserted_id
print("  Inserted student record Brooke Davidson into the students collection with document_id " + str(Brooke_student_id))


input("\n\n  End of program, press any key to exit... ")