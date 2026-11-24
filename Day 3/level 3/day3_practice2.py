#Level 3 – Practical real-world problem.
#Mini programming challenge

'''Exercise 8 – Simple ATM transaction system

Build a basic ATM simulation using loops and conditional statements.

Your program should:
1. Start with a balance of ₹10,000.
2. Display a menu:
   - 1. Check balance
   - 2. Deposit money
   - 3. Withdraw money 
   - 4. Exit
3. Allow the user to select an option.
4. For deposits, increase the balance.
5. For withdrawals, check whether sufficient balance exists.
6. Continue displaying the menu until the user selects Exit.
7. Display a suitable message for an invalid option.
Example interaction:
Welcome to ATM

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice: 1
Your balance is: 10000

Enter your choice: 2
Enter deposit amount: 2000
Amount deposited successfully.

Enter your choice: 1
Your balance is: 12000

Enter your choice: 4
Thank you for using our ATM.''' 


print("Welcome to ATM\n")

balance = 10000
print("Your available balance: ",balance)

while True:
  print("\nDisplay a Menu\n 1. Check balance\n 2. Deposit money\n 3. Withdraw money\n 4. Exit\n ")

  option = int(input("Enter your choice: "))
   
  if option == 1:
   print("Your available balance: ", balance)

  elif option == 2:
     amount = int(input("Enter the amount: "))
     if amount > 0:
      balance += amount
      print("Amount deposited successfully and your balance: ", balance)
     else:
      print("Invalid Number")

  elif option == 3:
     amount = int(input("Enter the amount: "))
     if amount > 0:
       if balance >= amount:
         balance -= amount
         print("Amount withdrawn successfully and your balance: ", balance)
       else:
        print("Insufficient balance")
     else:
      print("Invalid Number")

  elif option == 4:
      print("Thank you for using our ATM")
      break 
  
  else:
      print("Invalid option. Please try again.")   
