

"""1️⃣ Collection
👉 Meaning
A collection is any object that can hold multiple elements.
In Python, collections include:"""

# list
# tuple
# set
# dict
# string
# range
# etc.

# Key property:
# len(collection)

# Example:
# a = [1,2,3]
# b = (1,2,3)
# c = {1,2,3}
# d = "abc"

# all are collections
# 📌 Collection is a broad umbrella term.

"""
2️⃣ Sequence
👉 Meaning
A sequence is an ordered collection that supports:
"""

# Indexing
# Slicing
# Iteration
# Length

# Sequence types:
# Type
# list
# tuple
# string
# range
# Example:
s = "python"

print(s[0])     # p
print(s[1:4])   # yth

# Set and dict are not sequences because they are unordered.

"""
3️⃣ Iterator
👉 Meaning
An iterator is an object that produces values one at a time using:
"""

__iter__()
__next__()

# Key properties:
# Lazy evaluation
# Can be consumed only once
# Does NOT support indexing

# Example:
nums = [1,2,3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3


# After that:
next(it)  # StopIteration error

# Common iterators:
map()
filter()
reversed()
zip()
enumerate()
# generator

"""
4️⃣ List
👉 Meaning
"""

# A list is:
# A collection
# A sequence
# NOT an iterator

# List properties:
# Feature	List
# Ordered	✅
# Mutable	✅
# Indexable	✅
# Iterable	✅
# Iterator itself	❌
# Example:
lst = [10,20,30]

print(lst[1])   # 20


# But:
# next(lst)  # ❌ error


# Because list is iterable, not iterator.
# To make it iterator:

it = iter(lst)

"""
🔁 Relationship Diagram (Concept)
Collection
 ├── Sequence
 │    ├── List
 │    ├── Tuple
 │    ├── String
 │    └── Range
 ├── Set
 ├── Dict
 └── Others
 """

"""
Iterator (separate behavior layer)
 └── Created from collections or generators
 """

# 🔹 Key Differences Table

"""
| Feature      | Collection | Sequence | Iterator | List |
| ------------ | ---------- | -------- | -------- | ---- |
| Ordered      | maybe      | ✅        | maybe    | ✅    |
| Indexing     | maybe      | ✅        | ❌        | ✅    |
| Slicing      | maybe      | ✅        | ❌        | ✅    |
| One-time use | ❌          | ❌        | ✅        | ❌    |
| Mutable      | maybe      | maybe    | ❌        | ✅    |
| Is iterable  | ✅          | ✅        | ✅        | ✅    |
"""

# 🔹 Practical Example
lst = [1,2,3]

print(isinstance(lst, list))       # True
print(isinstance(lst, tuple))      # False

it = iter(lst)

print(type(it))   # iterator

# 🔹 Sequence vs Iterator
s = "abc"
it = iter(s)

print(s[0])     # works
print(next(it)) # works

print(s[1])     # works
print(next(it)) # moves forward


# Iterator forgets past values.
# Sequence remembers all values.

# 🔹 Why iterator is memory efficient
nums = range(1000000000)

# range stores only formula, not all numbers.

list(nums)  # creates huge memory usage

# 🔹 Interview One-liners

"""
✔ List is a sequence and a collection but not an iterator
✔ Iterator is a stateful object consumed once
✔ Sequence supports indexing and slicing
✔ Collection is a general container term
✔ Iterable ≠ Iterator
"""

# 🔹 Iterable vs Iterator (Bonus)
lst = [1,2,3]      # iterable
it = iter(lst)     # iterator

iter(it) is it     # True
