# ✅ What Is an Algorithm?
"""
An algorithm is a step-by-step procedure to solve a problem.
Examples:
    1. Sorting a list
    2. Searching for an element
    3. Finding the shortest path
    4. Solving mathematical problems
"""
# Algorithms are judged using:
"""
Time Complexity → how fast?
Space Complexity → how much memory?
"""

# ⭐ Types of Algorithms (with Python Examples)
# We categorize algorithms into major types used in coding + interviews.

# 1️⃣ Brute Force Algorithms
"""
Try all possibilities until the solution is found.
Example: Find the largest number in a list
"""
arr = [3, 8, 1, 9, 5]
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num
print(max_val)   # 9

# 2️⃣ Divide and Conquer Algorithms
"""
Break the problem → Solve smaller parts → Combine results.
Examples:
✔ Merge Sort
✔ Quick Sort
✔ Binary Search
"""
# Example: Binary Search (works only on sorted array)

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
print(binary_search([1, 2, 3, 4, 5, 6], 4))  # 3

# 3️⃣ Greedy Algorithms
# Make the best choice at each step, hoping it leads to the optimal solution.
# Example: Coin Change (minimum coins)

def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count
print(coin_change([1,5,10,25], 63))  # 6

# 4️⃣ Dynamic Programming (DP)
# Solve problems by breaking them into overlapping subproblems
# → Store (memoize) results for reuse.
# Example: Fibonacci (DP)

def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
print(fib(10))   # 55

# 5️⃣ Backtracking Algorithms
# Try a solution → if it fails, backtrack and try another.
# Example: N-Queens (simplified)

def solve(nums):
    res = []
    def backtrack(path, remaining):
        if not remaining:
            res.append(path)
            return
        for num in remaining:
            new_rem = remaining.copy()
            new_rem.remove(num)
            backtrack(path + [num], new_rem)
    backtrack([], nums)
    return res

print(solve([1, 2, 3]))

# ********************************************************************************
# ********************************************************************************
# ********************************************************************************

# 6️⃣ Searching Algorithms
# ✔ Linear Search
# ✔ Binary Search
# ✔ DFS
# ✔ BFS
# Example: Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
print(linear_search([5,3,7,1], 7))  # 2

# 7️⃣ Sorting Algorithms
# ✔ Bubble Sort
# ✔ Selection Sort
# ✔ Insertion Sort
# ✔ Merge Sort
# ✔ Quick Sort
# Example: Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

print(insertion_sort([9,5,1,4,3]))

# 8️⃣ Graph Algorithms
# Used for networks, maps, social graphs.
# Popular ones:
"""
1. DFS (Depth-First Search)
2. BFS (Breadth-First Search)
3. Dijkstra's Algorithm
4. Bellman-Ford
5. Floyd-Warshall
6. Minimum Spanning Tree (Kruskal, Prim)
"""

# Example: BFS
from collections import deque
def bfs(graph, start):
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        print(node, end=" ")

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

graph = {
    1: [2,3],
    2: [4],
    3: [5],
    4: [],
    5: []
}
bfs(graph, 1)

# 9️⃣ Recursive Algorithms
# A function calls itself to solve smaller instances.
# Example: Factorial

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(5))  # 120

# 🔟 Hashing Algorithms
# Use hash functions to store/retrieve data quickly.
# Example: Counting frequency using a dictionary

def freq(words):
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count

print(freq(["a","b","a","c","b","a"]))

# 1️⃣1️⃣ Two-Pointer Algorithms
def is_palindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("racecar"))

# 🎉 Summary Table

"""
| Algorithm Type      | Purpose                 | Example       |
| ------------------- | ----------------------- | ------------- |
| Brute Force         | Try all possibilities   | Max number    |
| Divide & Conquer    | Split & combine         | Binary Search |
| Greedy              | Local best choice       | Coin change   |
| Dynamic Programming | Overlapping subproblems | Fibonacci DP  |
| Backtracking        | Try / undo              | N-Queens      |
| Searching           | Find element            | DFS, BFS      |
| Sorting             | Arrange data            | Quick Sort    |
| Graph Algorithms    | Networks/maps           | Dijkstra      |
| Recursive           | Self-calling            | Factorial     |
| Hashing             | Fast lookup             | Frequency map |
| Two Pointer         | Efficient array ops     | Palindrome    |
"""
