'''1. Positive or negative

Take a number from the user and check whether it is positive, negative or zero.'''

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


'''2. Even or odd

Take a number and check whether it is even or odd.

Hint: Use the modulus operator %.'''

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


'''3. Largest of two numbers

Take two numbers and print the largest.'''

Number1 = int(input("Enter the first number: "))
Number2 = int(input("Enter the second number: "))

if Number1 > Number2:
    print(f"The largest number is: {Number1}")
else:
    print(f"The largest number is: {Number2}")


'''4. Voting eligibility

Take the user's age and check whether they are eligible to vote.'''

user_age = int(input("Enter the age of the user: "))

if user_age >= 21:
  print("user is eligible to vote")
else:
  print("user is not eligible to vote")


'''5. Largest of three numbers

Take three numbers and find the largest using conditional statements.'''

Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))

if Num1 >= Num2 and Num1 >= Num3:
    print(f"The largest number is: {Num1}")
elif Num2 >= Num1 and Num2 >= Num3:
    print(f"The largest number is: {Num2}")
else:
    print(f"The largest number is: {Num3}")


'''6. Grade calculator

Take marks from the user and print the grade using the grading system we studied.'''

user_marks = int(input("Enter the marks obtained: "))

if user_marks >= 90:
    print("Grade A")
elif user_marks >= 80:
    print("Grade B")
elif user_marks >= 70:
    print("Grade C")
elif user_marks >= 60:
    print("Grade D")
else:
    print("Fail")



'''7. Leap year

Take a year and determine whether it is a leap year.

Hint: A year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.'''

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



'''8. Login system

Set a username and password in your program. Ask the user to enter both and display:
- Login successful.
- Invalid username or password.'''

username = "avika"
password = "avika10"

user_username = input("Enter your username: ")
user_password = input("Enter your password: ")

if user_username == username:
    if user_password == password:
        print("Login successful.")
    else:
        print("Invalid password.")
else:
    print("Invalid username.")