# we will discuss the in-built data structures such as lists, tuples, dictionaries, etc. and some user-defined data
# structures such as linked lists, trees, graphs, etc.
#
# 1. List
# List is a built-in dynamic array which can store elements of different data types. It is an ordered collection of item,
# that is elements are stored in the same order as they were inserted into the list. List stores references to the objects
# (elements) rather than storing the actual data itself.



# 2. Searching Algorithms
# Searching algorithms are used to locate a specific element within a data structure, such as an array, list, or tree.
# They are used for efficiently retrieving information in large datasets.

import bisect
a = [2, 4, 6, 8, 10]

# Linear search using 'in'
print(6 in a)

# Linear search using 'count'
print(a.count(7) > 0)

# Binary search using bisect
pos = bisect.bisect_left(a, 8)
print("Found at index:", pos)

# 3. Sorting Algorithms
# Sorting algorithms are used to arrange the elements of a data structure, such as an array, list, or tree, in a particular
# order, typically in ascending or descending order. These algorithms are used for organizing data, which enables more efficient
# searching, merging, and other operations.