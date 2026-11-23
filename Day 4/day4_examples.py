'''Example 1 – Count vowels in a string
A vowel is one of these letters: a, e, i, o, u.'''

word = input("Enter a string: ")

count = 0
for ch in word.lower():
    if ch in "aeiou":
        count += 1
print(f"The number of vowels in the string is: {count}")


'''Example 2 – Reverse a string using a loop'''

string = input("Enter a string: ")
reversed_string = ""
for ch in string:
    reversed_string = ch + reversed_string
print(f"The reversed string is: {reversed_string}")


'''Example 3 – Check whether a string is a palindrome'''

string = input("Enter a string: ")
reverse = string[::-1]
if string == reverse:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")


'''Example 4 – Count the number of words'''

sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"The number of words in the sentence is: {len(words)}")
    