# Functions and Recursion in Python

import numbers


def sum(a,b):
    s = a + b
    return s

print(sum(5, 10))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calc_avg(numbers):
    i=0
    total = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1

    count = len(numbers)
    return total / count
    
print("Factorial of 5:", factorial(5))
numbers = [1, 2, 3, 4, 5]
print("Average of numbers:", calc_avg(numbers))

# Built in functions
print("Absolute value of -10:", abs(-10))
print("Maximum of (3, 7, 2, 9):", max(3, 7, 2, 9))
print("Minimum of (3, 7, 2, 9):", min(3, 7, 2, 9))
print("Power of 2^3:", pow(2, 3))
print("Rounding 5.67:", round(5.67))
print("Type of 100:", type(100))
print("Is 'Hello' an instance of str?:", isinstance("Hello", str))
print("Converting '123' to int:", int("123"))

def cal_prod(a=2,b=4):
    return a*b

print("Product with default args:", cal_prod())
print("Product with custom args:", cal_prod(3,5))

# Recursion 

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci of 7:", fibonacci(7))

#recursion uses stack memory
#function uses heap memory
# heap memory is like a large pool of memory used for dynamic allocation
# stack memory is used for static memory allocation and function call management

# Nested Functions
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()
print("Nested function output:", outer_function("hello"))