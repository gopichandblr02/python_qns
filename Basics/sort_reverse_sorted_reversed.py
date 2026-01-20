# sort vs sorted with examples
# sort() method sorts the list in place and returns None
# sorted() function returns a new sorted list from the elements of any iterable
# Example of sort() method


# 🔹 sort() vs sorted()
"""1. list.sort()"""

# 👉 Method of list object
# 👉 Sorts in-place
# 👉 Returns None

nums = [5, 2, 9, 1]
nums.sort()

print(nums)   # [1, 2, 5, 9]


# ❌ Return value: None

print(nums.sort())   # None

# Works only on:
# Lists

"""2. sorted()"""
#
# 👉 Built-in function
# 👉 Works on any iterable
# 👉 Returns a new list

nums = [5, 2, 9, 1]
res = sorted(nums)

print(res)    # [1, 2, 5, 9]
print(nums)   # [5, 2, 9, 1]  (original unchanged)

# Works on:
# list
# tuple
# string
# set
# dictionary keys

# 🔹 Examples by Data Type
# List
lst = [3, 1, 4]

print(sorted(lst))   # [1,3,4]
lst.sort()
print(lst)           # [1,3,4]

# Tuple
t = (3, 1, 4)
print(sorted(t))    # [1,3,4]
# t.sort() ❌ not allowed

# String
s = "python"
print(sorted(s))    # ['h','n','o','p','t','y']


# To get string back:

print("".join(sorted(s)))   # hnopty

# Set
st = {5,1,4}
print(sorted(st))  # [1,4,5]

# Dictionary
d = {"b":2, "a":1, "c":3}
print(sorted(d))        # ['a','b','c']
print(sorted(d.items()))  # [('a',1),('b',2),('c',3)]

# 🔹 Custom Sorting
data = [(1,3), (2,1), (4,2)]

print(sorted(data, key=lambda x: x[1]))
# [(2,1),(4,2),(1,3)]


# Reverse order:

print(sorted(data, key=lambda x:x[1], reverse=True))

"""🔹 reverse() vs reversed()"""
# 1. list.reverse()

# 👉 In-place
# 👉 Returns None

lst = [1,2,3]
lst.reverse()
print(lst)   # [3,2,1]

# 2. reversed()
#
# 👉 Built-in function
# 👉 Returns an iterator
# 👉 Does NOT modify original

lst = [1,2,3]

r = reversed(lst)
print(list(r))   # [3,2,1]
print(lst)       # [1,2,3]

# 🔹 On Strings
# s = "hello"

print(list(reversed(s)))      # ['o','l','l','e','h']
print("".join(reversed(s)))   # olleh

# 🔹 On Tuples
t = (1,2,3)
print(tuple(reversed(t)))   # (3,2,1)

# 🔹 Key Difference: Reverse vs Sort
lst = [3,1,4]

lst.reverse()      # just flips order
print(lst)         # [4,1,3]

lst.sort()         # sorts by value
print(lst)         # [1,3,4]

# 🔹 Interview Comparison Table
"""
| Feature           | sort()      | sorted()     |
| ----------------- | ----------- | ------------ |
| Type              | List method | Built-in     |
| Modifies original | ✅           | ❌            |
| Returns           | None        | New list     |
| Works on          | Only list   | Any iterable |

| Feature           | reverse()   | reversed()   |
| ----------------- | ----------- | ------------ |
| Type              | List method | Built-in     |
| Modifies original | ✅           | ❌            |
| Returns           | None        | Iterator     |
| Works on          | Only list   | Any iterable |
"""

# 🔹 Combined Example
s = "dbca"

print("".join(sorted(s)))        # abcd
print("".join(reversed(sorted(s))))  # dcba

# 🔹 Memory Perspective

"""
sorted() → new list in memory
sort()   → same list rearranged

reversed() → iterator object
reverse()  → same list rearranged
"""

# 🔹 When to use what?

"""
✔ Use sort() when you want to modify original list
✔ Use sorted() when you want original unchanged
✔ Use reverse() when order must change in-place
✔ Use reversed() when you just want iteration in reverse
"""

intervals=[[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x: x[0])
# other examples for key based sorting
# intervals.sort(key=lambda x: x[1])  # Sort by end time
# intervals.sort(key=lambda x: x[1]-x[0])  # Sort by duration
# sort by length of list of list
intervals.sort(key=len)