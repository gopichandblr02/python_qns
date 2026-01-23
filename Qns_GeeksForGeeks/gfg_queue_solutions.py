"""
queue_solutions.py

Solutions for the Top 50 Problems on Queue Data Structure asked in SDE Interviews.
Based on the GeeksforGeeks list:
https://www.geeksforgeeks.org/dsa/top-50-problems-on-queue-data-structure-asked-in-sde-interviews/
"""

from collections import deque
import math
import heapq
from typing import List, Deque, Tuple

# ----------------------------------------
# 1) Circular Array Implementation
# ----------------------------------------
class CircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.capacity = k
        self.front = self.rear = -1

    def enqueue(self, val) -> bool:
        if (self.rear + 1) % self.capacity == self.front:
            return False
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = val
        return True

    def dequeue(self):
        if self.front == -1:
            return None
        val = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return val

# ----------------------------------------
# 2) Linked List Implementation
# ----------------------------------------
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class LinkedQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        node = ListNode(val)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = node

    def dequeue(self):
        if not self.front:
            return None
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

# ----------------------------------------
# 3) Flipping Bits with K-Window
# ----------------------------------------
def min_flips_k_window(arr: List[int], k: int) -> int:
    flips = 0
    flip_marks = [0]*len(arr)
    curr_flip = 0
    for i in range(len(arr)):
        if i >= k:
            curr_flip ^= flip_marks[i-k]
        if (arr[i] ^ curr_flip) == 0:
            if i + k > len(arr):
                return -1
            flips += 1
            curr_flip ^= 1
            flip_marks[i] = 1
    return flips

# ----------------------------------------
# 4) Interleave the first and second halves
# ----------------------------------------
def interleave_queue(q: Deque[int]) -> Deque[int]:
    half = len(q)//2
    st = []
    for _ in range(half):
        st.append(q.popleft())
    while st:
        q.appendleft(st.pop())
    for _ in range(half):
        q.append(q.popleft())
    return q

# ----------------------------------------
# 5) Check if a queue can be sorted
# ----------------------------------------
def can_sort_queue(q: Deque[int]) -> bool:
    # Only possible if no decreases remain after consecutive rotations
    prev = q[0]
    for i in range(1, len(q)):
        if q[i] < prev:
            return False
        prev = q[i]
    return True

# ----------------------------------------
# 6) Generate Binary Numbers
# ----------------------------------------
def generate_binary(n: int) -> List[str]:
    q = deque(["1"])
    result = []
    for _ in range(n):
        s1 = q.popleft()
        result.append(s1)
        q.append(s1 + "0")
        q.append(s1 + "1")
    return result

# ----------------------------------------
# 7) Implement Stack using Queues
# ----------------------------------------
class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft() if self.q else None

# ----------------------------------------
# 8) Implement Stack using Two Queues
# ----------------------------------------
class StackTwoQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

# ----------------------------------------
# 9) Implement Queue using Two Stacks
# ----------------------------------------
class QueueTwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

# ----------------------------------------
# 10) Implement a Queue using a Stack
# ----------------------------------------
class QueueUsingStack:
    def __init__(self):
        self.s = []

    def enqueue(self, x):
        self.s.insert(0, x)

    def dequeue(self):
        return self.s.pop() if self.s else None

# ----------------------------------------
# 11) Reverse a queue using recursion
# ----------------------------------------
def reverse_queue(q: Deque[int]):
    if not q:
        return q
    val = q.popleft()
    reverse_queue(q)
    q.append(val)
    return q

# ----------------------------------------
# 12) Minimum steps to reach target by a Knight
# ----------------------------------------
def min_knight_steps(src: Tuple[int,int], dst: Tuple[int,int]) -> int:
    dirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    q = deque([(src[0], src[1], 0)])
    visited = set([src])
    while q:
        x,y,d = q.popleft()
        if (x,y) == dst:
            return d
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny,d+1))
    return -1

# ----------------------------------------
# 13) First negative integer in every window of size k
# ----------------------------------------
def first_negative_in_window(arr: List[int], k: int) -> List[int]:
    q = deque()
    res = []
    for i,val in enumerate(arr):
        if val < 0:
            q.append(i)
        if i >= k-1:
            while q and q[0] < i-k+1:
                q.popleft()
            res.append(arr[q[0]] if q else 0)
    return res

# ----------------------------------------
# 14) Minimum time to rot all oranges
# ----------------------------------------
def oranges_rot_time(grid: List[List[int]]) -> int:
    q = deque()
    fresh = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append((i,j,0))
            elif grid[i][j] == 1:
                fresh += 1
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    time = 0
    while q:
        x,y,t = q.popleft()
        time = max(time, t)
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]==1:
                grid[nx][ny]=2
                fresh -= 1
                q.append((nx,ny,t+1))
    return time if fresh==0 else -1

# ----------------------------------------
# 15) Shortest safe route in a path with landmines
# ----------------------------------------
def shortest_safe_route(grid: List[List[int]]) -> int:
    m,n = len(grid), len(grid[0])
    safe = [[True]*n for _ in range(m)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                for dx,dy in dirs:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n:
                        safe[nx][ny]=False
    q=deque([(0,0,0)]) if safe[0][0] else deque()
    visited=set()
    while q:
        x,y,d=q.popleft()
        if (x,y)==(m-1,n-1):
            return d
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and safe[nx][ny] and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny,d+1))
    return -1

# ----------------------------------------
# 16) First circular tour that visits all petrol pumps
# ----------------------------------------
def circular_tour(petrol: List[int], dist: List[int]) -> int:
    start=0
    deficit=0
    balance=0
    for i in range(len(petrol)):
        balance += petrol[i]-dist[i]
        if balance < 0:
            start = i+1
            deficit += balance
            balance=0
    return start if balance+deficit>=0 else -1

# ----------------------------------------
# 17) Reverse First k of Queue
# ----------------------------------------
def reverse_first_k(q: Deque[int], k: int) -> Deque[int]:
    st=[]
    for _ in range(k):
        st.append(q.popleft())
    while st:
        q.appendleft(st.pop())
    for _ in range(len(q)-k):
        q.append(q.popleft())
    return q

# ----------------------------------------
# 18) First non‑repeating in a Stream
# ----------------------------------------
def first_non_repeating(stream: str) -> List[str]:
    freq={}
    q=deque()
    res=[]
    for ch in stream:
        freq[ch]=freq.get(ch,0)+1
        q.append(ch)
        while q and freq[q[0]]>1:
            q.popleft()
        res.append(q[0] if q else '#')
    return res

# ----------------------------------------
# 19) Snake and Ladder Problem
# ----------------------------------------
def snake_ladder_min_moves(board: List[int]) -> int:
    n=len(board)
    q=deque([(0,0)])
    visited={0}
    while q:
        pos,moves=q.popleft()
        if pos==n-1:
            return moves
        for dice in range(1,7):
            nxt=pos+dice
            if nxt<n:
                if board[nxt]!=-1:
                    nxt=board[nxt]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves+1))
    return -1

# ----------------------------------------
# 20) Minimum Cost Path via given intermediates
# ----------------------------------------
def min_cost_path(adj: List[List[Tuple[int,int]]], src: int, dst: int) -> int:
    # adj: node-> [(neighbor,cost)]
    dist={src:0}
    pq=[(0,src)]
    while pq:
        cost,u=heapq.heappop(pq)
        if u==dst:
            return cost
        for v,w in adj[u]:
            new=cost+w
            if new < dist.get(v, math.inf):
                dist[v]=new
                heapq.heappush(pq,(new,v))
    return -1
