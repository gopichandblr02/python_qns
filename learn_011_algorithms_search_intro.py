"""What is a Search Algorithm?
A search algorithm is used to find an element in a data structure (list, tree, graph, etc.).
⭐ Types of Search Algorithms
There are two major categories:"""
# A. Search in Arrays / Lists
"""    
    Linear Search
    Binary Search
    Jump Search
    Interpolation Search
    Exponential Search
"""
# B. Search in Trees / Graphs
"""    
    Depth-First Search (DFS)
    Breadth-First Search (BFS)
    A* Search
    Dijkstra’s Algorithm
"""

# ✅ A. Search Algorithms for Arrays (with Python examples)
# 1️⃣ Linear Search (Sequential Search)
"""
Checks each element one by one.
Works on unsorted lists.
Time Complexity: O(N)
"""
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
print(linear_search([4,2,7,1,9], 7))   # Output: 2

# 2️⃣ Binary Search
"""
Works only on a sorted list
Divide list into halves
Fastest array search algorithm
Time Complexity: O(log N)
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([1, 2, 3, 4, 5, 6], 4))  # Output: 3

# 3️⃣ Jump Search
"""
Works on sorted arrays
Jumps by √n steps
Faster than linear search
Time Complexity: O(√n)
"""
import math
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
print(jump_search([1,2,3,4,5,6,7,8], 6))


# 4️⃣ Interpolation Search
"""
Improved version of binary search
Works best on uniformly distributed sorted data
Time Complexity: O(log log N) best case
Worst: O(N)
"""
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1

        pos = low + ((target - arr[low]) * (high - low) //
                     (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
print(interpolation_search([10, 20, 30, 40, 50], 40))

# 5️⃣ Exponential Search
"""
Useful for unbounded or infinite lists
First find range → then binary search
Time Complexity: O(log N)
"""

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2

    left, right = i//2, min(i, n-1)
    return binary_search(arr[left:right+1], target)

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(exponential_search([1,2,3,4,5,6,7,8], 7))


# ✅ B. Search in Trees and Graphs (with Python)
# 6️⃣ DFS (Depth-First Search)
"""
Go deep along one branch
Implemented using stack/recursion
"""
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    "A": ["B","C"],
    "B": ["D","E"],
    "C": ["F"],
    "D": [], "E": [], "F": []
}

dfs(graph, "A")

# 7️⃣ BFS (Breadth-First Search)
"""
Explore level by level
Uses a queue
"""

from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start])

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

graph = {
    1: [2,3],
    2: [4],
    3: [5],
    4: [], 5: []
}

bfs(graph, 1)

# 8️⃣ Dijkstra’s Algorithm
# Finds shortest path in weighted graph (no negative weights).

import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

graph = {
    "A":[("B",1),("C",4)],
    "B":[("C",2),("D",5)],
    "C":[("D",1)],
    "D":[]
}

print(dijkstra(graph, "A"))

# 9️⃣ A* Search
# Used in pathfinding (maps, games).

#-------------

"""
| Search Algorithm     | Works On                   | Sorted? | Time Complexity |
| -------------------- | -------------------------- | ------- | --------------- |
| Linear Search        | List                       | ❌       | O(N)            |
| Binary Search        | List                       | ✔       | O(logN)         |
| Jump Search          | List                       | ✔       | O(√N)           |
| Interpolation Search | Uniform List               | ✔       | O(log log N)    |
| Exponential Search   | Large/Infinite List        | ✔       | O(log N)        |
| DFS                  | Graph/Tree                 | N/A     | O(V+E)          |
| BFS                  | Graph/Tree                 | N/A     | O(V+E)          |
| Dijkstra             | Weighted Graph             | N/A     | O(E log V)      |
| A* Search            | Weighted Graph + Heuristic | N/A     | O(E log V)      |
"""
