### python_tips

#### 1. Tips for loops
- arr=  [1,2,3,4,5,6]
- Index  0,1,2,3,4,5
- Here length = 6, last_element = arr[-1] or arr[5] or arr[arr_length-1]
```
for x in range(arr_len):
    print(arr[x])
```
- To skip first element
```
for x in range(1,arr_len):
    print(arr[x])
```
or
```
for x in arr[1:]:
    print(x)
```

- Reverse
```
arr=[16, 17, 4, 3, 5, 2]
a = arr[-1:0:-1] or arr[-1::-1] or arr[::-1]
print(a)
```
#### 2. reverse() vs reversed()
🔹 1. reverse() — In-place list method

- Works only on lists.
- Modifies the original list.
- Returns None (it doesn’t create a new list).

Example:
```nums = [1, 2, 3, 4]
nums.reverse()
print(nums)
```

Output: [4, 3, 2, 1]


✅ Notes:
- You can’t use .reverse() on strings or tuples — it will raise an AttributeError.
- It changes the existing list in place.

🔹 2. reversed() — Built-in function

- Works on any sequence (lists, strings, tuples, ranges, etc.).
- Returns a reverse iterator — not a list or string. 
- You can convert it to a list, tuple, or string if needed.

Example 1 — List
```nums = [1, 2, 3, 4]
rev_nums = reversed(nums)
print(list(rev_nums))  # Convert iterator to list
```
Output:
[4, 3, 2, 1]


✅ Original list is unchanged:
print(nums)  # [1, 2, 3, 4]

Example 2 — String
```word = "hello"
rev_word = reversed(word)
print(''.join(rev_word))  # join converts iterator back to string
```

```
# List examples
lst = [1, 2, 3]
lst.reverse()
print(lst)  # [3, 2, 1]

lst = [1, 2, 3]
print(list(reversed(lst)))  # [3, 2, 1]
print(lst)  # [1, 2, 3] (unchanged)

# String example
s = "python"
print(''.join(reversed(s)))  # nohtyp

```

#### 3. sort vs sorted 

🔹 list.sort() — In-place method
- Modifies the original list (no new list created)
- Works only on lists
- Returns None
- More memory efficient (no copy created)

Example:
```
nums = [5, 2, 9, 1]
nums.sort()
print(nums)
```
Output:[1, 2, 5, 9]

✅ Original list is changed.
If you print the return value:
print(nums.sort())  # None

Optional parameters:
nums.sort(reverse=True)  # Descending order
nums.sort(key=len)       # Sort by length (if list of strings)

🔹 sorted() — Built-in function
- Works on any iterable (lists, strings, tuples, sets, dicts, etc.)
- Returns a new sorted list
- Does not modify the original data
- Returns a list (even if input is a string or tuple)

Example:
```nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 5, 9]
print(nums)         # [5, 2, 9, 1] (unchanged)
```

Works with any iterable
```print(sorted("python"))   # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted((3, 1, 2)))  # [1, 2, 3]
print(sorted({3, 5, 1}))  # [1, 3, 5]
```

Optional parameters:

Same as sort():
sorted(nums, reverse=True)
sorted(words, key=len)
