'''Question 1: Personal introduction

Write a program that displays:

My name is Abhi
I am a Computer Science student
I want to become a Software Engineer ''' 

print("My name is Abhi")
print("I am a Computer Science student")
print("I want to become a Software Engineer")



'''Question 2: Store student details

Create variables for:
- Name
- Age
- College
- Branch
- CGPA
Print all five details.'''

Name = "Abhi"
Age = 20
College = "Siddhartha Institute of Technology and Sciences"
Branch = "Computer Science"
CGPA = 7.8

print("Name:", Name)
print("Age:", Age)
print("College:", College)  
print("Branch:", Branch)
print("CGPA:", CGPA)


'''Question 3: Add two numbers

Take two numbers as input and display their sum.

Example:
Enter first number: 10
Enter second number: 20
Sum = 30'''

First_number = 10
Second_number = 5

print("Sum =", First_number + Second_number)


'''Question 4: Age calculator

Ask the user for their current age and calculate their age after five years.'''

current_age = int(input("Enter your current age: "))

print("Age after Five years:", current_age + 5)


''' Question 5: Rectangle calculator

Take length and breadth as input.

Calculate:
- Area = length × breadth
- Perimeter = 2 × (length + breadth) '''

Length = int(input("Enter the length of the rectangle: "))
Breadth = int(input("Enter the breadth of the rectangle: "))

Area = Length * Breadth
Perimeter = 2 * (Length + Breadth)

print("Area of the Rectangle :", Area)
print("Perimater of the Rectangle :", Perimeter)


'''Question 6: Simple bill calculator

Ask for:
- Product name
- Price
- Quantity
Calculate the total bill.'''

Product_name = input("Enter the product name: ")
Price = float(input("Enter the price of the product: "))
Quantity = int(input("Enter the quantity of the product: "))

Total_bill = Price * Quantity

print(f"Total bill for {Quantity} {Product_name}(s) is: {Total_bill}")


'''Question 7: Temperature conversion

Convert Celsius into Fahrenheit.

Formula:  F = frac{9}{5}C + 32

'''

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9/5) * celsius + 32

print("Celsius is equal to Fahrenheit:", fahrenheit)


'''Question 8: Swap two variables

Given:
a = 10
b = 20

Swap their values so that a = 20 and b = 10.'''

a = 10
b = 20  

a, b = b, a

print("After swapping: a =", a, "b =", b)

