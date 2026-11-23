#Level 2 – Beginner to intermediate
#3 PROGRAMS

'''Exercise 5 – Sum of natural numbers

Take a number n from the user and calculate the sum of all numbers from 1 to n.

Example:
Input: 5
Output: 15


Hint: Maintain a variable called total.'''

number = int(input("Enter a number: "))

i = 1
total = 0

while i <= number:
    total += i
    i += 1
print(f"The sum of all numbers from 1 to {number} is: {total}")


'''Exercise 6 – Factorial of a number

Write a program to calculate the factorial of a number using a loop.

Example:
Input: 5
Output: 120

Remember: 5! = 5 x 4 x 3 x 2 x 1

Hint: Start with a result of 1 and multiply it by successive numbers.'''

number = int(input("Enter a number: "))
result = 1
for i in range(1, number+1):
    result *= i
print(f"The factorial of {number} is: {result}")


'''Exercise 7 – Prime number checking

Take a number from the user and check whether it is prime.

Example:
Input: 7
Output: Prime number


Input: 8
Output: Not a prime number


Hint: Check whether any number other than 1 and itself divides the given number. Consider how break can help.'''
 
number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print("Not a prime number")
