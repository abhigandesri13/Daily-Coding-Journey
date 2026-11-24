#Level 3 – Practical real-world challenge
#Mini project

'''Exercise 8 – Username and email validation

Build a simple registration input validator.

Requirements:
1. Ask the user to enter a username.
2. Check that the username contains at least 5 characters.
3. Ask the user to enter an email address.
4. Check whether the email contains @.
5. Check whether the email ends with .com.
6. Display whether the entered information passes these basic checks.
Example:
Enter username: abhi123
Enter email: abhi@gmail.com

Username: Valid
Email: Valid
Registration details accepted.


Try to use:
- len()
- lower()
- strip()
- find() or in
- endswith()
- if-else
Note: This is a beginner validation exercise, not a complete production-grade email validator.'''

while True:
    username = input("Enter username: ").strip()
    if len(username) >= 5:
        break
    else:
        print("Username: Invalid")

while True:
    email = input("Enter email: ").strip().lower()
    if "@" in email and email.endswith(".com"):
        break
    else:
        print("Email: Invalid")

print("\nUsername: Valid")
print("Email: Valid")
print("Registration details accepted.")