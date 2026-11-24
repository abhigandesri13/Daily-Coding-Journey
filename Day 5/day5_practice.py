#Level 1 – Basic exercises

# 1. Create a list of five numbers and print the list and its length.

list = [5, 10, 15, 20, 25]

print(list)
print("Length: ", len(list))   



# 2. Print the first, last and third elements of a list.

list = [5, 10, 15, 20, 25]

print("First element: ", list[0])
print("Last element: ", list[-1])
print("Third element: ", list[2])



# 3. Print the first three and last two elements using slicing.

list = [5, 10, 15, 20, 25]

print("First three elements: ", list[:3])
print("Last two elements: ", list[-2:])



# 4. Create a fruit list and add two fruits using append() and insert().

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
fruits.insert(2, "grape")

print(fruits)