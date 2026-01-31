# Loops

# While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
print("While loop ended.")

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
print("For loop ended.")

# Looping through a range
for i in range(5):
    print("Number:", i)
print("Range loop ended.")

# Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
print("Nested loops ended.")

# Loop with else
for num in range(3):
    print("Number in loop:", num)
else:
    print("Loop ended without break.")

# Break and Continue
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    if i == 1:
        print("Continuing at i =", i)
        continue
    print("Current i:", i)
print("Loop with break and continue ended.")

# Using pass in loops
for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    print("i in pass loop:", i)
print("Pass loop ended.")

# Looping through a dictionary
student = {"name": "Alice", "age": 22, "course": "Physics"}
for key, value in student.items():
    print(f"{key}: {value}")
print("Dictionary loop ended.")

i=100
while i != 0:
    print(i)
    i -= 1
print("Countdown finished.")

num = int(input("Enter a number to find its multiplication table: "))
for j in range(11):
    print(f"{num} x {j} = {num * j}")

heroes = ["Superman", "Batman", "Wonder Woman"]

idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

facto = int(input("Enter a number to find its factorial: "))
result = 1
for k in range(1, facto + 1):
    result *= k
print(f"The factorial of {facto} is {result}")