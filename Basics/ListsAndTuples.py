# Lists and Tuples

marks = [100, 97.4, 80.4, 24, 56.7, 78, 88.9
]
print(marks)
print(type(marks))
print(len(marks))
print(marks[2])
print(marks[-1])

student = ["John", 21, "A"]
print(student)
student[0] = "Jane"
print(student)
print(student[0:2])  # Slicing
print(student[::-1])  # Reversing

# List Methods
list = [1, 2, 3]
list.append(4)
print("After append:", list)
list.insert(1, 1.5)
print("After insert:", list)
list.remove(2)
print("After remove:", list)
popped_item = list.pop()
print("After pop:", list, "Popped item:", popped_item)
list.sort(reverse=True)
print("After sort:", list)
list.reverse()
print("After reverse:", list)


# Tuples
coordinates = (10.0, 20.0)
print(coordinates)

print(type(coordinates))
print(len(coordinates))
print(coordinates[1])
print(coordinates[-1])
print(coordinates.index(20.0))
print(coordinates.count(10.0))






