#Level 1 – Easy exercises
#4 PROGRAMS


'''Exercise 1 – Print numbers

Write a Python program to print numbers from 1 to 20 using a for loop.'''

for i in range(1, 21):
    print(i)

'''Exercise 2 – Even numbers

Write a program to print all even numbers between 1 and 50 using a for loop.'''

for i in range(1, 51):
    if i % 2 == 0:
        print(i)



'''Exercise 3 – Multiplication table 

Take a number from the user and print its multiplication table from 1 to 10.

Example: Input = 5.

Expected output:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50'''

number = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")



'''Exercise 4 – Countdown

Use a while loop to print numbers from 10 down to 1 and then print "Happy New Year!".'''

i = 10
while i >= 1:
    print(i)
    i -= 1
print("Happy New Year!")