# from database import load_data, save_data
# def add_student():
#     students = load_data()

#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     course = input("Enter Course: ")
#     marks = int(input("Enter Marks: "))

#     student = {
#         "name": name,
#         "age": age,
#         "course": course,
#         "marks": marks
#     }
 
#     students.append(student)
#     save_data(students)

#     print("Student Added Successfully")

# def view_students():
#     students = load_data()

#     if len(students) == 0:
#         print("No Student Found")
#         return

#     print("-" * 60)
#     print(f"{'Name':<20}{'Age':<10}{'Course':<15}{'Marks':<10}")
#     print("-" * 60)

#     for student in students:
#         print(
#             f"{student['name']:<20}"
#             f"{student['age']:<10}"
#             f"{student['course']:<15}"
#             f"{student['marks']:<10}"
#         )

# def search_student():
#     students = load_data()

#     name = input("Enter Student Name: ")

#     for student in students:
#         if student["name"].lower() == name.lower():

#             print("Student Found")
#             print(student)

#             return

#     print("Student Not Found")

# def update_student():
#     students = load_data()

#     name = input("Enter Student Name To Update: ")

#     for student in students:

#         if student["name"].lower() == name.lower():

#             student["age"] = int(input("New Age: "))
#             student["course"] = input("New Course: ")
#             student["marks"] = int(input("New Marks: "))

#             save_data(students)

#             print("Student Updated Successfully")

#             return

#     print("Student Not Found")

# def delete_student():
#     students = load_data()

#     name = input("Enter Student Name To Delete: ")

#     for student in students:

#         if student["name"].lower() == name.lower():

#             students.remove(student)

#             save_data(students)

#             print("Student Deleted Successfully")

#             return

#     print("Student Not Found")

from database import load_data, save_data

def add_student():
    students = load_data()

    name = input("Enter Name: ")

    # Duplicate Check
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Already Exists")
            return

    # Age Validation
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Please Enter Valid Age")

    course = input("Enter Course: ")

    # Marks Validation
    while True:
        try:
            marks = int(input("Enter Marks: "))
            break
        except ValueError:
            print("Please Enter Valid Marks")

    student = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_data(students)

    print("Student Added Successfully")


def view_students():
    students = load_data()

    if len(students) == 0:
        print("No Student Found")
        return

    print("-" * 60)
    print(f"{'Name':<20}{'Age':<10}{'Course':<15}{'Marks':<10}")
    print("-" * 60)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['age']:<10}"
            f"{student['course']:<15}"
            f"{student['marks']:<10}"
        )


def search_student():
    students = load_data()

    name = input("Enter Student Name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            print("\nStudent Found")
            print("-" * 35)
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            print("Marks  :", student["marks"])
            print("-" * 35)

            return

    print("Student Not Found")


def update_student():
    students = load_data()

    name = input("Enter Student Name To Update: ")

    for student in students:

        if student["name"].lower() == name.lower():

            while True:
                try:
                    student["age"] = int(input("New Age: "))
                    break
                except ValueError:
                    print("Please Enter Valid Age")

            student["course"] = input("New Course: ")

            while True:
                try:
                    student["marks"] = int(input("New Marks: "))
                    break
                except ValueError:
                    print("Please Enter Valid Marks")

            save_data(students)

            print("Student Updated Successfully")

            return

    print("Student Not Found")


def delete_student():
    students = load_data()

    name = input("Enter Student Name To Delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            confirm = input("Are you sure? (Y/N): ")

            if confirm.lower() != "y":
                print("Delete Cancelled")
                return
 
            students.remove(student)

            save_data(students)

            print("Student Deleted Successfully")

            return

    print("Student Not Found")
