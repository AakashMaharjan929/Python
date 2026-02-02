# Class and object example in Python

class Student:
    def __init__(self, fullname):
        print("This is a constructor")
        self.name = fullname
    
    def getMarks(self, marks):
        self.marks = marks
        return self.marks

# Creating an object of the Student class
student1 = Student("Aakash Maharjan")
# Accessing the class variable through the object
print(student1.name)
marks_obtained = student1.getMarks(85)
print("Marks obtained:", marks_obtained)

class Car:
    color = "Blue"
    brand = "Mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

# Class and instance attributes example
class Person:
    Subject = ["Python", "Java", "C++"]
    name="anonymous"
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

person1 = Person("John", 30)
print(person1.name)
print(person1.age)
person2 = Person("Alice", 25)
print(person2.name)
print(person2.age)
print(Person.Subject)
print(person1.Subject)
print(person2.Subject)

personAnonymous = Person("",0)
print(Person.name)

# Static method 
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
result = MathOperations.add(5, 10)
print("Sum:", result)

# Abstraction, Encapsulation, Inheritance, and Polymorphism example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

my_car = ElectricCar("Tesla", "Model S", 100)

my_car.display_info()





