"""map() and filter()
Both map() and filter() functions are designed to be lazy, returning iterators (map object and filter object, respectively).
This approach is memory efficient, especially when dealing with large datasets, as it calculates results only as
needed (e.g., in a loop or when explicitly converted).
To get a list, you must explicitly convert the iterator using the list() constructor, which consumes the iterator:"""

numbers = [1, 2, 3, 4, 5]

# map returns an iterator
mapped_iterator = map(lambda x: x * 2, numbers)
mapped_list = list(mapped_iterator) # [2, 4, 6, 8, 10]

# filter returns an iterator
filtered_iterator = filter(lambda x: x % 2 == 0, numbers)
filtered_list = list(filtered_iterator) # [2, 4]

"""
reduce()
The reduce() function applies a rolling computation to sequential pairs of values in an iterable, ultimately returning a 
single, cumulative value. It does not return a list or an iterator. 
reduce() is located in the functools module and must be imported
"""

from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]

# reduce returns a single value (sum of all numbers)
result = reduce(operator.add, numbers) # 15


"""🔹 1. map()
👉 Purpose
Apply a function to each element of an iterable."""

# 👉 Syntax
# map(function, iterable)

# Returns a map object (iterator).
# Example 1: Square numbers
nums = [1, 2, 3, 4]

res = map(lambda x: x*x, nums)
print(list(res))   # [1, 4, 9, 16]

# How it works:
"""
1 → 1*1 → 1
2 → 2*2 → 4
3 → 3*3 → 9
4 → 4*4 → 16
"""

# Example 2: Convert strings to int
data = ["1", "2", "3"]
print(list(map(int, data)))   # [1,2,3]

# Example 3: Multiple iterables
a = [1,2,3]
b = [4,5,6]

print(list(map(lambda x,y: x+y, a, b)))
# [5,7,9]


# filter(function, iterable)

# 🔹 2. filter()
# 👉 Purpose
# Select elements that satisfy a condition.
# 👉 Syntax
# Function must return True or False.

# Example 1: Even numbers
nums = [1,2,3,4,5,6]

res = filter(lambda x: x%2==0, nums)
print(list(res))   # [2,4,6]

# Example 2: Words longer than 4 letters
words = ["python","is","very","easy"]

print(list(filter(lambda w: len(w)>4, words)))
# ['python']

# Example 3: Remove empty strings
data = ["hi", "", "hello", ""]

print(list(filter(None, data)))
# ['hi','hello']


# None filters out falsy values.

"""
🔹 3. reduce()
👉 Purpose
Reduce all elements into one single value.

👉 From module
from functools import reduce

👉 Syntax
reduce(function, iterable)

Example 1: Sum
"""
from functools import reduce

nums = [1,2,3,4]

res = reduce(lambda x,y: x+y, nums)
print(res)   # 10

"""
Step-by-step:
1+2 = 3
3+3 = 6
6+4 = 10
"""

# Example 2: Product
reduce(lambda x,y: x*y, [1,2,3,4])  # 24

# Example 3: Max element
reduce(lambda x,y: x if x>y else y, [5,2,9,1])
# 9

# 🔹 Data Type Examples
# String with map
s = "abc"
print(list(map(str.upper, s)))  # ['A','B','C']

# Tuple with filter
t = (10,15,20,25)
print(tuple(filter(lambda x:x%20==0, t)))
# (20,)

# 🔹 Using list comprehensions instead
# map → list comprehension
[x*x for x in nums]

# filter → list comprehension
[x for x in nums if x%2==0]

# reduce → loop
total = 0
for x in nums:
    total += x

# 🔹 When to use which?

"""| Task                   | Best   |
| ---------------------- | ------ |
| Transform elements     | map    |
| Select elements        | filter |
| Aggregate to one value | reduce |"""

# 🔹 Combined Example
nums = [1,2,3,4,5,6]

result = reduce(lambda x,y: x+y,
                filter(lambda x:x%2==0,
                       map(lambda x:x*x, nums)))

print(result)

# Meaning:
# Square → keep even → sum
# [1,4,9,16,25,36] → [4,16,36] → 56

# 🔹 Interview Notes

"""
✔ map/filter return iterators
✔ reduce is in functools
✔ list comprehensions are more Pythonic
✔ reduce useful for aggregation
✔ All support lazy evaluation
"""

"""
🔹 Memory Diagram (Concept)
map → iterator → list()
filter → iterator → list()
reduce → single value
"""