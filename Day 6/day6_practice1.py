# Level 2 – Beginner/intermediate exercises

# 5. Given two sets, find their union, intersection and difference.

first_set = {1, 2, 3, 4, 5}
second_set = {3, 4, 5, 6, 7}

print("Union: ", first_set | second_set)
print("Intersection: ", first_set & second_set)
print("Difference: ", first_set - second_set)
print("Differnce(Second set - First set): ", second_set - first_set)


# 6. Create a dictionary of five students and their marks. Find the student with the highest marks.

student = {
    "Abhi" : 90,
    "shivani" : 95,
    "sai" : 80,
    "sudheer" : 70,
    "Akash" : 65
}

highest_marks = 0
name_id = ""
for name, marks in student.items():
    if marks > highest_marks:
        highest_marks = marks
        name_id = name

print("Name: ", name_id)
print("Highest_marks: ", highest_marks)


# 7. Given a list of numbers, count the frequency of each number using a dictionary.

numbers = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
       frequency[num] = 1

print(frequency)


