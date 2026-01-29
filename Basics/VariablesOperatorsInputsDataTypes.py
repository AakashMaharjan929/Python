# variables and Data Types

print("My name is Aakash Maharjan") 
print("Hello world")
print("Python","is","Super")
print(25)
print(24+96)
name="Amir"
age=25
price=25.99
print("Name:",name)
print("Age:",age)   
print("Price:",price)

name1="Shraddha"
name2='Shraddha'
name3='''Shraddha'''
print(name1)
print(name2)
print(name3)

# Data types
name="Aakash"          # String
age=25                 # Integer
price=25.99           # Float
is_student=True      # Boolean
print(type(name))
print(type(age))
print(type(price))
print(type(is_student))

# Multiple assignment
x, y, z = 10, 20.5, "Hello"
print(x)
print(y)
print(z)

# Constants
PI = 3.14159

print("Value of PI:", PI)

# Comments
# This is a single-line comment

'''
This is a multi-line comment
spanning multiple lines.
It is used for documentation.
'''

a=2
b=5
sum=a+b
print("Sum:",sum)

 
A,B = 2,3
Txt = "@"
print(2*Txt*3)

A,B="2",3
Txt="@"
print((A+Txt)*B)

# Integer division
num1 = 1.5
num2 = 3
print(num1//num2)

#modulo operator
print(-5%2)

#input in Python

# String input
name = input("Enter your name: ")

#int input

age = int(input("Enter your age: "))

#float input
price = float(input("Enter the price: "))

print(name, age, price)

#Types of operator

# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Comparison Operators
x = 5
y = 10
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal To:", x >= y)  
print("Less Than or Equal To:", x <= y)

# Logical Operators
p = True
q = False
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

# Assignment Operators
num = 10
num += 5
print("After += :", num)
num *= 2
print("After *= :", num)
num -= 4
print("After -= :", num)
num /= 2
print("After /= :", num)
num %= 3
print("After %= :", num)
num **= 2
print("After **= :", num)
num //= 2
print("After //= :", num)

# Bitwise Operators
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print("AND:", a & b)   # Binary: 0001
print("OR:", a | b)    # Binary: 0111
print("XOR:", a ^ b)   # Binary: 0110
print("NOT a:", ~a)    # Binary: 1010
print("Left Shift a by 1:", a << 1)  # Binary: 1010
print("Right Shift a by 1:", a >> 1) # Binary: 0010

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in list?", 3 in my_list)
print("Is 6 not in list?", 6 not in my_list)

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)
print("x is z:", x is z)
print("x is not z:", x is not z)

# Conditional Statements
#if elif else

light = input("light: ")
if (light=="red"):
    print("Stop")
elif (light=="yellow"):
    print("Look")
else:
    print("Go")

# Ternary operator
age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Clever if
age=18
vote = ("yes", "no")[age<18]
print("Can vote:", vote)

#Type conversion and 
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print("String:", num_str)
print("Integer:", num_int)
print("Float:", num_float)

a= 2
b= 4.8

print(a+b)
