# Strings and Conditional Statements in Python

str1 = "This is a string."
str2 = 'Shraddha'
str3 = """This is a multi-line string. """

#escape sequences
str4 = "This is a string with a newline character.\nSee?"
str5 = 'It\'s a beautiful day!'
str6 = "He said, \"Hello!\""
str7 = "This is a backslash: \\"
str8 = "This is a tab:\tSee the space?"
str9 = "This is a carriage return:\rSee?"
str10 = "This is a form feed:\fSee?"
str11 = "This is a vertical tab:\vSee?"
str12 = "This is a backspace: \bSee?"

# Concatenation
greeting = "Hello, " + "world!"

# length of string
length_of_str1 = len(str1)

print(str11)
print("Length of str1:", length_of_str1)
print(str1[1])

# Slicing
sliced_str = str2[1:5]  # 'hrad'
print("Sliced string:", sliced_str)
#negative indexing
last_char = str2[-1]  # 'a'

# String Functions
str="I am a coder."
print(str.upper())          # 'I AM A CODER.'
print(str.lower())          # 'i am a coder.'
print(str.capitalize())     # 'I am a coder.'
print(str.title())          # 'I Am A Coder.'
print(str.count('a'))      # 2
print(str.find('coder'))   # 7
print(str.replace('coder', 'developer'))  # 'I am a developer.'
print(str.split())         # ['I', 'am', 'a', 'coder.']
print(str.strip('.'))      # 'I am a coder'
print(str.isalpha())       # False
print(str.isdigit())       # False
print(str.startswith('I am'))  # True
print(str.endswith('coder.'))  # True
print(str.index('a'))      # 2
print(str.rfind('a'))     # 5
print(str.zfill(20))      # '0000000000I am a coder.'
print(str.center(30, '*'))  # '**********I am a coder.**********'
print(str.swapcase())      # 'i AM A CODER.'
print(str.partition('a'))  # ('I ', 'a', 'm a coder.')
print(str.encode())        # b'I am a coder.'
print(str.expandtabs())   # 'I am a coder.'
print(str.islower())      # True    
print(str.isupper())      # False
print(str.istitle())      # False
print(str.isprintable())  # True
print(str.maketrans('coder', 'developer'))  # {99: 100, 111: 101, 100: 118, 101: 108, 114: 111}
print(str.translate(str.maketrans('coder', 'developer')))  # 'I am
print(str.removeprefix('I am '))  # 'a coder.'
print(str.removesuffix('.'))  # 'I am a coder'
print(str.partition(' '))  # ('I', ' ', 'am a coder.')
print(str.rpartition(' '))  # ('I am a', ' ', 'coder.')
print(str.splitlines())    # ['I am a coder.']
print(str.isascii())      # True
print(str.isidentifier()) # False
print(str.isnumeric())    # False
print(str.isdecimal())    # False
print(str.isalnum())      # False

# Conditional Statements
# if-elif-else
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Nested if
age = 25
if age >= 18:
    if age < 65:
        print("Adult")
    else:
        print("Senior Citizen")
else:
    print("Minor")

# Ternary Operator
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)



