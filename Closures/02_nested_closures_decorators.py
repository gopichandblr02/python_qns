# 1. Nested Functions
# A nested function is simply a function defined inside another function.
# Example
def outer():
    def inner():
        print("Hello from inner")
    inner()

# Purpose
# ✔ Code organization
# ✔ Helper logic not needed outside
# ✔ Avoid polluting global namespace

# Key Point
# Nested function ≠ closure (unless it captures outer variables)

# 2. Closures
# A closure is a nested function that remembers variables from its enclosing scope even after the outer function finishes.
# Example
def outer(x):
    def inner():
        return x
    return inner

f = outer(10)
print(f())   # 10


# Here:
# x belongs to outer
# inner captures x
# Even after outer exits, inner remembers x

# Why closures matter
# ✔ Data hiding
# ✔ Functional programming style
# ✔ Callbacks, factories
# ✔ Avoid global variables

# Interview definition
# Closure = function + preserved lexical environment

# 3. Decorators
# A decorator is a closure that wraps another function to extend behavior without modifying it.
# Example
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi")

say_hi()

# Output
# Before
# Hi
# After

# What happened internally
say_hi = my_decorator(say_hi)


# So decorator = closure + function replacement.

# Relationship
"""
| Concept         | What it is                                    |
| --------------- | --------------------------------------------- |
| Nested function | Function inside another function              |
| Closure         | Nested function that captures outer variables |
| Decorator       | Closure that wraps another function           |

"""

"""
Nested Function
      ↓
   Closure
      ↓
  Decorator
"""



# Not all nested functions are closures.
# Not all closures are decorators.
# All decorators use closures.

# Side-by-Side Example
# Nested (no closure)
def outer():
    y = 10
    def inner():
        print("Hello")
    inner()

# Closure
def outer(y):
    def inner():
        return y
    return inner

# Decorator
def deco(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

# Practical Use Cases
"""
Feature	            Use case
Nested	            Helper logic
Closure	            Cache, state preservation
Decorator	        Logging, auth, timing, validation
"""

# Real FAANG-style Example
# Timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper

# One-line summary
#
# Nested functions organize code.
# Closures preserve state.
# Decorators enhance behavior.