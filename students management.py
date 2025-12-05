students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        for roll, info in students.items():
            print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        info = students[roll]
        print(f"Found: Name: {info['name']}, Marks: {info['marks']}\n")
    else:
        print("Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        marks = float(input("Enter new Marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student updated successfully.\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")

def top_student():
    if not students:
        print("No student records to evaluate.\n")
    else:
        top = max(students.items(), key=lambda x: x[1]['marks'])
        print(f"Top Student: Roll: {top[0]}, Name: {top[1]['name']}, Marks: {top[1]['marks']}\n")

def main():
    while True:
        print("1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Top Student\n7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            top_student()
        elif choice == '7':
            print("Exiting program.")

            break
        else:
            print("Invalid choice. Try again.\n")
main()  

















          