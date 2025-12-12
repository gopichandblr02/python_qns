# __init__ is one of the most important concepts in Python OOP.
# Here is the simplest, cleanest explanation:
# 🔹 What is __init__ in Python?
# __init__ is a special method in Python called the constructor of a class.
# It runs automatically when you create (instantiate) an object from that class.
# 🔹 Why do we use __init__?
# To initialize (set up) the object’s data.
# Example:
# When you create a student, you want to give it a name, age.
# When you create a node, you want to give it a value.
# __init__ sets up these values when the object is created.
# 🔹 Simple Example
# class Person:
#     def __init__(self, name, age):
#         self.name = name      # attribute
#         self.age = age

# p = Person("John", 25)
# print(p.name)   # John
# print(p.age)    # 25
# What happened?
#
# Person("John", 25) → Python automatically calls __init__(self, "John", 25)
# Inside the method, we store those inside the object as self.name, self.age.
# 🔹 self in __init__
# self refers to the current object
# You use it to store attributes on that object.
# Example
# self.value = value
# Means:
# "Store value inside THIS object."

# 🔹 What happens behind the scenes?
# When you write:
# p = Person("John", 25)
# Python does:
# Create an empty object p
# Call the __init__ method on it
# Set p.name = "John"
# Set p.age = 25
#
# 🔹 Another Example (Linked List Node)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# This means:
# Every node starts with a value
# And next pointer is set to None initially
# 🔹 If a class has no __init__?
# Python provides a default constructor.
# 🔹 Quick Analogy
# __init__ is like:
# Setting up furniture when you move into a new house
# Preparing the object with necessary data

###############################################################################
####################### Default Constructor ###################################
###############################################################################
class Test:
    pass
obj = Test()
print("Object created:", obj)

class Student:
    def hello(self):
        print("Hello from Student")

s = Student()   # default constructor used
s.hello()

# 🔹 Example 3: Add attributes later
# Objects can still have attributes even without __init__.

class Person:
    pass
p = Person()      # default constructor
p.name = "John"   # adding attributes manually
p.age = 30

print(p.name, p.age)


