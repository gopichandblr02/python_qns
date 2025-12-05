"""
🔥 Sorting in Python — Introduction
Sorting means arranging data in a specific order (ascending or descending).
Example:"""
nums = [5, 3, 8, 1]
sorted_nums = sorted(nums)
# [1, 3, 5, 8]
print(sorted('abdc'))
['a', 'b', 'c', 'd']

"""
Sorting helps in:
1. Searching efficiently (Binary Search needs sorted data)
2. Removing duplicates
3. Solving many coding interview problems
4. Grouping, merging, optimization tasks
"""

# 2. Removing duplicates -> Example
arr = [4, 1, 7, 1, 4, 2]
arr.sort()

result = []
for num in arr:
    if not result or result[-1] != num:
        result.append(num)

print(result)  # [1, 2, 4, 7]

# *************
"""
Binary Search is a fast searching algorithm used to find an element in a sorted array or list.
It works by repeatedly dividing the search interval in half — this gives it a time complexity of O(log n), which is 
much faster than linear search (O(n)).
"""

# 🚀 How Binary Search Works
# Start with two pointers:
nums=[1, 2, 4, 7]
n=len(nums)
left = 0
right = n - 1
# Find the middle index:
mid=(left+right)//2
"""Compare the target value with arr[mid]:
If equal → found
If target < arr[mid] → search left half
If target > arr[mid] → search right half

Continue until left > right."""

# ✅ Iterative Binary Search — Python

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # Check middle element
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    return -1   # Not found
arr = [1, 3, 5, 7, 9, 12, 15]
target = 9
print(binary_search(arr, target))   # Output: 4


# ✅ Recursive Binary Search — Python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [2, 4, 6, 8, 10, 12]
print(binary_search_recursive(arr, 8, 0, len(arr)-1))   # Output: 3


# ✅ Example
# Array must be sorted:
arr = [2, 5, 8, 12, 16, 23, 38, 56]
target = 23

# Steps:
# mid = 3 → arr[3] = 12 → 23 > 12 → search right half
# mid = 5 → arr[5] = 23 → found 🎉

# 🧠 Python Code (Iterative)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # not found
"""
📌 Time & Space Complexity
Time: O(log n)
Space: O(1)
"""
# 🎯 When to Use Binary Search
# Use it when:
"""The data is sorted
You need fast lookup"""
# Not suitable for:
"""Unsorted data (unless you sort first)
Linked lists (random access needed)"""

# *************



"""
⭐ Built-in Sorting in Python
1️⃣ sorted(iterable)
Returns a new sorted list.
"""

nums = [4, 2, 8, 1]
print(sorted(nums))

# Output:
[1, 2, 4, 8]

"""
2️⃣ .sort()
Sorts in place and returns None.
"""

nums = [4, 2, 8, 1]
nums.sort()
print(nums)

"""3️⃣ Sorting in reverse"""
nums.sort(reverse=True)

# 4️⃣ Sorting with key
words = ["apple", "banana", "cat"]
words.sort(key=len)

"""📌 Key Terms in Sorting
Term	                    Meaning
Stable Sort	                Keeps original order of equal elements
In-place	                Uses O(1) or small extra space
Comparison-based	        Uses < or > to compare elements
Time Complexity	            How fast the algorithm works
"""

#
#*******🔥 Most Popular Sorting Algorithms*******
#


#################################################################
####Below are the main sorting algorithms used in interviews.####
#################################################################

"""1️⃣ Bubble Sort"""
# Simple but slow.
# ✔ Idea
# Repeatedly compare adjacent elements and swap if out of order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ⏱ Complexity

"""Time: O(n²)
Space: O(1)
Stable: Yes"""

"""2️⃣ Selection Sort"""
# Select the smallest and place it at beginning.
# ✔ Idea
# Find minimum → put at index 0
# Find next minimum → put at index 1 …

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

"""⏱ Complexity"""
# Time: O(n²)
# Space: O(1)
# Stable: No

"""3️⃣ Insertion Sort"""
# Useful for nearly sorted arrays.
# ✔ Idea
# Pick an element → insert it into correct position in sorted part.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

"""⏱ Complexity"""
# Time: O(n²)
# Best Case: O(n)
# Space: O(1)
# Stable: Yes

"""4️⃣ Merge Sort"""
# Efficient, divide-and-conquer.
# ✔ Idea
# Split array in half
# Sort each half
# Merge sorted halves

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ⏱ Complexity
"""
Time: O(n log n)
Space: O(n)
Stable: Yes
"""

"""5️⃣ Quick Sort"""
# Fastest in practice.
# ✔ Idea
# Pick a pivot
# Partition the array
# Recursively sort left & right partitions

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

# ⏱ Complexity
"""
Case    	Time
Best    	O(n log n)
Avg     	O(n log n)
Worst   	O(n²)
Space:      O(log n)
Stable:     No
"""

# 6️⃣ Heap Sort
"""Uses heap (priority queue).
✔ Idea
Build a max heap
Repeatedly extract max
Place at end of array"""


def heap_sort(arr):
    import heapq
    heap = []
    for x in arr:
        heapq.heappush(heap, x)
    return [heapq.heappop(heap) for _ in range(len(heap))]


"""(Note: Python’s heapq is min-heap)"""

# ⏱ Complexity

"""Time: O(n log n)
Space: O(n) or in-place version O(1)
Stable: No"""

# 7️⃣ Counting Sort
"""Works for small range of integers.
✔ Idea
Count occurrences of each number."""

def counting_sort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1)

    for num in arr:
        count[num] += 1

    result = []
    for num, c in enumerate(count):
        result.extend([num]*c)
    return result

# ⏱ Complexity

"""Time: O(n + k)**
Space: O(k)
Stable: Yes
k = range of numbers"""

# ⭐ Sorting Algorithm Comparison Table
"""
Algorithm   	Time (Avg)  	Space   	Stable  	In-Place
Bubble Sort 	O(n²)          	O(1)	    Yes        	Yes
Selection Sort	O(n²)	        O(1)	    No	        Yes
Insertion Sort	O(n²)	        O(1)	    Yes	        Yes
Merge Sort	    O(n log n)	    O(n)	    Yes	        No
Quick Sort	    O(n log n)	    O(log n)	No	        Yes
Heap Sort	    O(n log n)	    O(1)	    No	        Yes
Counting Sort	O(n+k)	        O(k)	    Yes	        No
"""
