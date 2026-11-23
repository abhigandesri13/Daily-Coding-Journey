#Level 2 – Beginner/intermediate
#3 PROGRAMS


'''Exercise 5 – Palindrome checker

Take a word and check whether it is a palindrome.

Example:
Input: madam
Output: Palindrome

Hint: Compare the original string with its reversed version. Consider case normalization.'''

word = input("Enter a word: ")
reverse = word[::-1]
if word.lower() == reverse.lower():
    print(f"{word} is a palindrome.")


'''Exercise 6 – Character frequency

Take a string and a character from the user.

Count how many times that character appears.

Example:
Input: programming
Character: m
Output: 2

Hint: Use a loop and a counter, or investigate the count() method.'''

string = input("Enter a string: ")
char = input("Enter a character to count: ")

count = 0
for ch in string.lower():
    if ch == char.lower():
        count += 1

print(f"The character '{char}' appears {count} times in the string.")


'''Exercise 7 – Remove vowels

Take a string and create a new string without any vowels.

Example:
Input: Education
Output: dctn


Hint: Create an empty string and append only characters that are not vowels.'''

string = input("Enter a string: ")
new_string = ""

for ch in string.lower():
    if ch not in "aeiou":
        new_string += ch
print(f"The string without vowels is: {new_string}")