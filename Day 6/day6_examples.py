# Practical coding examples

''' Program 1 – Remove duplicates from a list using a set
Problem: Given a list containing duplicate values, remove the duplicates. '''

numbers = [10, 20, 10, 30, 20, 40, 50]
unique_numbers = set(numbers)
print(unique_numbers)

''' Program 2 – Find common elements using sets '''

students_a = {"Abhi", "Rahul", "Kiran", "Ajay"}
students_b = {"Kiran", "Ajay", "Arun", "Vijay"}
common_students = students_a & students_b
print("Common students:", common_students)

''' Program 3 – Store and display student details using a dictionary '''

student = {
    "name": "Abhi",
    "age": 21,
    "branch": "CSE",
    "cgpa": 7.8
}
for key, value in student.items():
    print(key, ":", value)

'''Program 4 – Count the frequency of elements using a dictionary'''

numbers = [1, 2, 1, 3, 2, 1, 4, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)






# Mini project: Student Record Management System

''' Practical application

Build a small student record management system.

Your program should:
1. Add a student with their name and marks.
2. Search for a student.
3. Display all student records.
4. Update a student's marks.
5. Display the number of students.
6. Exit the program.   '''

students = {}

while True:

    print("\n--- Student Record Management ---")
    print("1. Add student")
    print("2. Search student")
    print("3. Display all students")
    print("4. Update marks")
    print("5. Total students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            continue

        marks = float(input("Enter student marks: "))

        students[name] = marks

        print("Student added successfully.")

    elif choice == "2":

        name = input("Enter student name to search: ").strip()

        if name in students:
            print("Student found.")
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == "3":

        if len(students) == 0:
            print("No student records available.")

        else:
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == "4":

        name = input("Enter student name: ").strip()

        if name in students:

            marks = float(input("Enter updated marks: "))
            students[name] = marks

            print("Marks updated successfully.")

        else:
            print("Student not found.")

    elif choice == "5":

        print("Total students:", len(students))

    elif choice == "6":

        print("Thank you!")
        break

    else:
        print("Invalid choice.")