"""

len(array) in Python — Time & Space Complexity
✅ Time Complexity: O(1) (Constant Time)
Calling len(array) in Python does NOT traverse the array.
Python lists store their length in a metadata field, so retrieving it is just a direct lookup.

Why O(1)?
A Python list internally keeps an integer that tracks its length.

len() simply returns that stored value.
No iteration, no computation → always constant time.

✅ Space Complexity: O(1)
len() does not allocate new memory proportional to the size of the array.
It only returns an integer (constant size).

"""