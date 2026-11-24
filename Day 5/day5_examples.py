# Program 1 – Calculate sum and average of list elements

list = [10, 20, 30, 40, 50]
sum = 0

for num in list:
    sum += num

average = sum / len(list)

print("Total: ", sum)
print("Average: ", average)


#Program 2 – Find the largest number 

list = [10, 20, 30, 40, 50]
largest = list[0]

for num in list:
    if num > largest:
        largest = num

print("Largest number is: ", largest)


#Program 3 – Count even and odd numbers

list = [10, 21, 32, 43, 54]
even_count = 0
odd_count = 0

for num in list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count: ", even_count)
print("Odd numbers count: ", odd_count)


#Program 4 – Search for an element

list = [10, 20, 30, 40, 50]

target = int(input("Enter a number to search: "))

if target in list:
    print("Number found in the list.")
else:
    print("Number not found in the list.")