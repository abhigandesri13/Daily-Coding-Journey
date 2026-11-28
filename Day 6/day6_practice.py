# Level 1 – Basic exercises

#1. Create a tuple containing five student details and print its first, last and third elements.

student_details = ("Abhi", 21, "CSE", 7.8, "India")

print("First element: ", student_details[0])
print("Last element: ", student_details[-1])
print("Third element: ", student_details[2])


# 2. Create a tuple containing repeated numbers and count how many times a particular number appears.

numbers = (1, 2, 3, 1, 4, 2, 1, 5)
print("Count of 1: ", numbers.count(1))


# 3. Create a set containing duplicate numbers and display the unique elements.

numbers = {1, 2, 3, 1, 4, 2, 1, 5}
print("Unique elements: ", numbers)


# 4. Create a dictionary containing your name, age, branch and CGPA. Display all key-value pairs.

student = {
    "name": "Abhi",
    "age": 21,
    "branch": "CSE",
    "cgpa": 7.8
}

print(student.items())