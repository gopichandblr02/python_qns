# def outer():
#     def inner():
#         print("Hello from inner")
#     inner()

# Here, inner() is called, but not returned.

# 🔹 Case 1 — inner()
def outer():
    def inner():
        print("Hello")
    inner()

x = outer()
print(x) # if we comment this line then only "Hello" will be printed
print('-----')

# Output
# Hello
# None

# Why?
# inner() executes.
# outer() returns nothing → None.
# So x = None.

# 🔹 Case 2 — return inner
def outer():
    def inner():
        print("Hello")
    return inner

x = outer()
print(x)
x()
print('-----')

# Output
# <function outer.<locals>.inner at 0x1057177e0>
# Hello

# Why?
# You return the function object.
# You can call it later.

# 🔹 Case 3 — return inner()
def outer():
    def inner():
        print("Hello")
    return inner()

x = outer()
print(x)
print('-----')

# Output
# Hello
# None

# Why?
# inner() runs immediately.
# Its return value (None) is returned.

# 🔹 Summary Table
"""
| Statement      | What happens                          |
| -------------- | ------------------------------------- |
| inner()        | Executes inner, outer returns None    |
| return inner   | Returns function reference            |
| return inner() | Executes inner and returns its output |

"""
# 🔹 Interview One-Liner

# inner() calls the function, return inner returns the function itself, and return inner() returns the result of the function call.

# 🔹 Closure Connection
def outer():
    x = 10
    def inner():
        print(x)
    return inner

f = outer()
f()   # prints 10
print('-----')

# Here return inner enables closure.