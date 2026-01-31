# Dictionary and Set
info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "subjects": ["Math", "Science", "Art"]
}
print(info)
print(type(info))
print(len(info))
print(info["name"])
print(info.get("age"))
print(info.keys())
print(info.values())
print(info.items())
info["age"] = 31
print("Updated age:", info["age"])
info["profession"] = "Engineer"
print("Added profession:", info["profession"])
del info["city"]
print("After deleting city:", info)
info.pop("subjects")
print("After popping subjects:", info)
info.update({"country": "USA"})
print("After updating country:", info)
info["Salary"] = 70000
print("After adding Salary:", info)

null_dict = {}
print("Empty dictionary:", null_dict)

# Nested Dictionary
student_info = {
    "student1": {
        "name": "Bob",
        "age": 22,
        "courses": ["History", "Math"]
    },
    "student2": {
        "name": "Carol",
        "age": 23,
        "courses": ["Biology", "Chemistry"]
    }
}
print("Nested dictionary:", student_info)
# Accessing nested dictionary
print("Student1's name:", student_info["student1"]["name"])
print("Student2's courses:", student_info["student2"]["courses"])

# Sets
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)
print(type(fruits))
print(len(fruits))
fruits.add("orange")
print("After adding orange:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)
fruits.discard("grape")  # No error if not found
print("After discarding grape:", fruits)
popped_fruit = fruits.pop()
print("After popping an element:", fruits, "Popped element:", popped_fruit)
fruits.clear()
print("After clearing the set:", fruits)
null_set = set()
print("Empty set:", null_set)

# Set Operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print("Set A:", setA)
print("Set B:", setB)
print("Union:", setA | setB)
print("Intersection:", setA & setB)
print("Difference (A - B):", setA - setB)
print("Symmetric Difference:", setA ^ setB)
print("Is A subset of B?:", setA.issubset(setB))
print("Is A superset of B?:", setA.issuperset(setB))
print("Are A and B disjoint?:", setA.isdisjoint(setB))
print("Frozenset example:")
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)
print("Type of frozenset:", type(frozen_set))
print("Length of frozenset:", len(frozen_set))
print("Is 2 in frozenset?:", 2 in frozen_set)
print("Is 5 in frozenset?:", 5 in frozen_set)
print("Iterating through frozenset:")
for item in frozen_set:
    print(item)
print("Set operations with frozenset:")
another_set = {3, 4, 5}
print("Union:", frozen_set | another_set)
print("Intersection:", frozen_set & another_set)
print("Difference (frozenset - another_set):", frozen_set - another_set)
print("Symmetric Difference:", frozen_set ^ another_set)
print("Is frozenset subset of another_set?:", frozen_set.issubset(another_set))
print("Is frozenset superset of another_set?:", frozen_set.issuperset(another_set))
print("Are frozenset and another_set disjoint?:", frozen_set.isdisjoint(
    another_set))
print("Minor")
print("Adding element to frozenset will raise an error.")
# Note: Frozensets are immutable, so you cannot add or remove elements.

