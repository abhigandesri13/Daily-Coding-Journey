#Level 2 – Beginner/intermediate

# 5. Find the sum and average of numbers in a list.

list = [5, 10, 15, 20, 25]
sum = 0
for num in list:
    sum += num

average = sum / len(list)

print("Total: ", sum)
print("Average: ", average)


# 6. Count how many times a particular number appears using count().

numbers = [1, 2, 3, 4, 5, 1, 2, 1]

print("Count of 1: ", numbers.count(1))


# 7. Sort a list of numbers in ascending and descending order.

numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()
print("Sorted in ascending order: ", numbers)

numbers.sort(reverse=True)
print("Sorted in descending order: ", numbers)