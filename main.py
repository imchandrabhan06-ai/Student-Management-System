import student
while True:

    print("\n")
    print("=" * 40)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 40)
 
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        student.add_student()

    elif choice == "2":
        student.view_students()

    elif choice == "3":
        student.search_student()

    elif choice == "4":
        student.update_student()

    elif choice == "5":
        student.delete_student()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")