"""
heapq.heappush(heap, item) is a function in Python's heapq module used to add a new value to a heap while preserving its min-heap property.

Key Features
Min-Heap Invariant: It ensures that the smallest element is always at the root (heap[0]).
Efficiency: The operation has a time complexity of O(log n), where n is the number of elements in the heap.
In-Place Modification: It modifies the provided list in-place rather than returning a new one.
"""

import heapq

# Initialize an empty heap
my_heap = []
# Push elements onto the heap
heapq.heappush(my_heap, 10)
heapq.heappush(my_heap, 5)
heapq.heappush(my_heap, 15)

# The smallest element is always at index 0
print(my_heap[0])  # Output: 5

###################################
###################################

my_heap = [5, 10, 15]
heapq.heapify(my_heap)

# Extract the smallest element
smallest = heapq.heappop(my_heap)

print(smallest)  # Output: 5
print(my_heap)   # Output: [10, 15] (remaining elements are re-sorted)
