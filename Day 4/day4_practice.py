###Level 1 – Easy exercises
###4 PROGRAMS

'''Exercise 1 – String information

Take a string from the user and display:
- Original string.
- Length of the string.
- First character.
- Last character.
- Uppercase version.
- Lowercase version.'''

string = input("Enter a string: ")

print("Original string:", string)
print("Length of the string:", len(string))
if len(string) > 0:
    print("First character:", string[0])
    print("Last character:", string[-1])
print("Uppercase version: ", string.upper())
print("Lowercase version: ", string.lower())


'''Exercise 2 – Character extraction

Take a word from the user and print:
- First three characters.
- Last three characters.
- Reversed string.'''

word = input("Enter a word: ")

print("First three characters:", word[:3])
print("Last three characters:", word[-3:])
print("Reversed string:", word[::-1])


'''Exercise 3 – Count vowels

Take a string and count the total number of vowels.

Example:
Input: Education
Output: 5 '''

word = input("Enter a string: ")

count = 0
for ch in word.lower():
    if ch in "aeiou":
        count += 1
print(f"The number of vowels in the string is: {count}")


'''Exercise 4 – Replace spaces

Take a sentence from the user and replace every space with a hyphen -.

Example:
Input: Python is easy
Output: Python-is-easy'''

sentence = input("Enter a sentence: ")
new_sentence = sentence.replace(" ", "-")
print("Modified sentence:", new_sentence)

