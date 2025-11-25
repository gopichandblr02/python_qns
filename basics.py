# The concept of a Python function returning another function is known as a closure

"""
✅ What is a Closure in Python?
A closure is a function that remembers variables from its enclosing (outer) function even after the outer function has finished executing.

In simple words:
➡️ A closure = inner function + variables from the outer function stored together.
Closures happen when:
You have a nested function (a function inside another function).
The inner function uses variables from the outer function.
The outer function returns the inner function.
"""

def outer():
    x = 10
    def inner():
        return x  # inner function uses x from outer function
    return inner  # return inner function (not calling)

fn = outer()
print(fn())  # prints 10

"""
How this works:
- outer() finishes running but before finishing, it returns inner().
- The returned function still remembers the value of x (this is the closure).
- Even though outer() is gone, x = 10 is preserved.
"""

# ✅ Practical Example 1: Creating a Counter
# Closures are commonly used to keep private state.

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment


c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3

# ✔ Why closure?
# count acts like a hidden private variable.
# Each call increments the stored value.

# ✅ Practical Example 2: Create a Multiplier Function

def make_multiplier(n):
    def multiply(x):
        return x*2 + n
    return multiply

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50

# ✔ Notice:
# times3 remembers n = 3
# times5 remembers n = 5
# This is function factory pattern (commonly used in functional programming).

# ✅ Practical Example 3: Logging Wrapper (Decorator-like)

def logger(msg):
    def log():
        print("Log:", msg)
    return log

log_hi = logger("Hello")
log_hi()  # Log: Hello

# Closure keeps msg even after outer function ends.
"""
| Use Case                 | Why Helpful                                  |
| ------------------------ | -------------------------------------------- |
| Hide / encapsulate state | Similar to private variables in OOP          |
| Function factories       | Create variations of functions               |
| Custom decorators        | Decorators rely heavily on closures          |
| Callback functions       | Useful for event-driven or async programming |
"""

def my_decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@my_decorator
def greet():
    print("Hi")

greet()

"""
🎯 Summary

A closure is formed when:

A function is nested inside another
The inner function uses variables from the outer function
The outer function returns the inner

Closures allow:

Private variables
Function factories
Decorators
Cleaner, more modular code
"""

####################################################################
############################## General Basics ######################
####################################################################
x =23/10   # 2.3
y=23//10   # 2  floor
a=321%10   # 1
print(1//10)  # 0
print(1%10)  # 1
print(1/10)  # 0.1
aa =1234
while aa:
    print(aa)
    aa=aa//10

for x in [1,2,8]:
    print(x)
# 1
# 2
# 8

# sep wont work for loops, it works for unpacking
for x in [1,2,8]:
    print(x,sep=";")
# 1
# 2
# 8

# Default separator is space
a=[1,2,3]
print(*a,sep=";")
# 1;2;3

# By default end is \n for loops
for x in a:
    print(x,end=",")
# 1,2,3,


print(10,20,30,sep=";")
# Output
#10;20;30

