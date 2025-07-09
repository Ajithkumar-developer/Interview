# Python String Operations and Methods - Examples with Definitions

```python
# Initial string
s = "hello world"
print("Initial string:", s)  # hello world

# capitalize(): Converts first character to uppercase
print("capitalize():", s.capitalize())  # Hello world

# upper(): Converts all characters to uppercase
print("upper():", s.upper())  # HELLO WORLD

# lower(): Converts all characters to lowercase
print("lower():", s.lower())  # hello world

# title(): Converts first character of each word to uppercase
print("title():", s.title())  # Hello World

# swapcase(): Swaps case of each character
print("swapcase():", s.swapcase())  # HELLO WORLD

# count(sub): Counts occurrences of a substring
print("count('l'):", s.count('l'))  # 3

# find(sub): Returns lowest index of substring or -1 if not found
print("find('world'):", s.find('world'))  # 6

# rfind(sub): Returns highest index of substring
print("rfind('l'):", s.rfind('l'))  # 9

# index(sub): Like find(), but raises error if not found
print("index('world'):", s.index('world'))  # 6

# startswith(prefix): Checks if string starts with prefix
print("startswith('hello'):", s.startswith('hello'))  # True

# endswith(suffix): Checks if string ends with suffix
print("endswith('world'):", s.endswith('world'))  # True

# isalpha(): Checks if all characters are alphabetic
print("'hello'.isalpha():", "hello".isalpha())  # True

# isdigit(): Checks if all characters are digits
print("'123'.isdigit():", "123".isdigit())  # True

# isalnum(): Checks if all characters are alphanumeric
print("'abc123'.isalnum():", "abc123".isalnum())  # True

# isspace(): Checks if all characters are whitespace
print("'   '.isspace():", "   ".isspace())  # True

# join(iterable): Joins elements of an iterable with the string as separator
print("'-'.join(['a', 'b', 'c']):", '-'.join(['a', 'b', 'c']))  # a-b-c

# split(sep): Splits the string into a list
print("s.split():", s.split())  # ['hello', 'world']

# rsplit(sep): Splits from the right
print("s.rsplit():", s.rsplit())  # ['hello', 'world']

# replace(old, new): Replaces substring with new one
print("s.replace('world', 'Python'):", s.replace('world', 'Python'))  # hello Python

# strip(): Removes leading and trailing whitespace
print("'  hello  '.strip():", '  hello  '.strip())  # hello

# lstrip(): Removes leading whitespace
print("'  hello'.lstrip():", '  hello'.lstrip())  # hello

# rstrip(): Removes trailing whitespace
print("'hello  '.rstrip():", 'hello  '.rstrip())  # hello

# format(): Formats string with placeholders
print("'{} is {} years old'.format('Alice', 30):", "{} is {} years old".format('Alice', 30))  # Alice is 30 years old

# f-string: Inline formatting
name = "Bob"
age = 25
print(f"{name} is {age} years old")  # Bob is 25 years old

# len(): Returns length of the string
print("len(s):", len(s))  # 11

# Slicing
print("s[0:5]:", s[0:5])  # hello

# Concatenation
s1 = "hello"
s2 = "python"
print("Concatenated:", s1 + " " + s2)  # hello python

# Repetition
print("Repetition:", s1 * 2)  # hellohello

# Membership
print("'world' in s:", 'world' in s)  # True

# Iteration
print("Iterating over string:")
for char in s:
    print(char, end=' ')  # h e l l o   w o r l d
print()
