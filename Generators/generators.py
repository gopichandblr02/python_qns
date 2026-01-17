# 🔹 What is a Generator in Python?

"""
A generator is a special type of function that returns an iterator and produces values one at a time using the yield
keyword instead of return.
It pauses execution, remembers its state, and resumes from where it left off.
Normal Function vs Generator
"""

def normal():
    return 1
    return 2

# ➡ Only returns once.

def gen():
    yield 1
    yield 2

# ➡ Produces values one by one.

# 🔹 How Generator Works (Execution Flow)
"""
Call generator()  → returns generator object
next() called     → runs till yield
State saved
next() again      → resumes after yield
"""

# 🔹 Example
def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

# 🔹 Generator Object Properties
print(type(g))  # <class 'generator'>


# Generator supports: So it is an iterator.
__next__()
__iter__()


# 🔹 Generator vs Return
"""
| return         | yield           |
| -------------- | --------------- |
| Ends function  | Pauses function |
| No state saved | State preserved |
| Single value   | Multiple values |
"""

# 🔹 Memory Advantage
# Normal list:

nums = [i for i in range(10_000_000)]

# Generator:
nums = (i for i in range(10_000_000))

# Generator consumes almost zero memory.
# 🔹 Generator Expressions

gen = (i*i for i in range(5))

for v in gen:
    print(v)

# Equivalent to:

def sq():
    for i in range(5):
        yield i*i

# 🔹 Yield with Loop
def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# 🔹 Generator State Preservation Example
def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

g = demo()

next(g)
next(g)
next(g)


# Output:
"""
Start
Middle
End
"""

# 🔹 Generator with return
def test():
    yield 1
    return 5

# Return raises StopIteration(5) internally.

# 🔹 StopIteration
g = test()
print(next(g))
print(next(g))  # StopIteration

# 🔹 Sending Data to Generator
def receiver():
    x = yield
    print("Received:", x)

g = receiver()
next(g)
g.send(10)

# 🔹 Generator with send()
def calculator():
    while True:
        x = yield
        print(x * x)

g = calculator()
next(g)
g.send(4)
g.send(5)

# 🔹 Yield From (Delegation)
def sub():
    yield 1
    yield 2

def main():
    yield from sub()
    yield 3

# 🔹 Generator for File Processing
def read_file(path):
    with open(path) as f:
        for line in f:
            yield line

# Memory efficient for huge files.

# 🔹 Infinite Generator
def infinite():
    i = 0
    while True:
        yield i
        i += 1

# 🔹 Generator vs List vs Iterator
"""
| Feature  | Generator | List | Iterator |
| -------- | --------- | ---- | -------- |
| Memory   | Low       | High | Low      |
| Reusable | No        | Yes  | No       |
| Lazy     | Yes       | No   | Yes      |
"""

# 🔹 Generator vs Iterator

# Iterator:

class MyIter:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 3:
            raise StopIteration
        self.i += 1
        return self.i


# Generator does same with:
def mygen():
    for i in range(1,5):
        yield i

# 🔹 Generator in Pipeline
def read():
    yield from range(10)

def square(nums):
    for i in nums:
        yield i*i

def even(nums):
    for i in nums:
        if i % 2 == 0:
            yield i

for v in even(square(read())):
    print(v)

# 🔹 Generator Use Cases
"""
| Use Case                  |
| ------------------------- |
| Streaming data            |
| File processing           |
| Infinite sequences        |
| Data pipelines            |
| Lazy evaluation           |
| Kafka consumer simulation |
| Big data processing       |
"""

# 🔹 Generator Pitfalls
"""
Cannot rewind
Single iteration
Exhausted after use
Cannot access by index
"""

# 🔹 When NOT to Use Generator
"""
When you need random access
When data must be reused
When dataset is small
"""
# 🔹 Generator in Interview
"""
Q: Why generators are faster?
A: They avoid memory allocation and use lazy evaluation.
"""

# 🔹 Diagram (Conceptual)
"""
Generator Function
       |
       v
Generator Object
       |
next()
       |
yield → value
       |
State saved
"""

# 🔹 Real Interview Example
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

# 🔹 Generator vs Coroutine

"""Generators become coroutines when using send()."""

# 🔹 Generator with try/finally
def gen():
    try:
        yield 1
        yield 2
    finally:
        print("Cleanup")

# 🔹 close()
g.close()
"""Calls finally block."""

# 🔹 throw()
g.throw(ValueError)

# 🔹 Summary
"""
| Feature          | Generator |
| ---------------- | --------- |
| Lazy evaluation  | Yes       |
| State memory     | Yes       |
| Memory efficient | Yes       |
| Iterable         | Yes       |
| Iterator         | Yes       |
"""
# 🔹 One-Line Definition

"""Generator is a function that produces a sequence of values lazily using yield and remembers 
its execution state between calls."""

########################################################################################################################
###########################################          Next Topics      ##################################################
########################################################################################################################

"""
✔ Generator vs async generator
✔ Generator internal stack frame diagram
✔ Generator interview Q&A
✔ Generator + Kafka streaming simulation
✔ Generator problems from LeetCode
✔ Generator with decorators
"""