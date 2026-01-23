"""
stack_solutions.py

Python implementations for Top 50 Stack problems from GeeksforGeeks:
Top 50 Problems on Stack Data Structure asked in SDE Interviews.

Reference: List of problems from GfG article (easy + medium + hard). :contentReference[oaicite:1]{index=1}
"""

import random
from typing import List, Optional

# ----------------------
# Basic Stack with Python List
# ----------------------

class Stack:
    """Simple stack implementation using Python list."""
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop() if self._data else None

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


# 1. Parenthesis Checker (Balanced Brackets)
def is_balanced(expr: str) -> bool:
    pairs = {')': '(', '}': '{', ']': '['}
    st = Stack()
    for ch in expr:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.is_empty() or st.pop() != pairs[ch]:
                return False
    return st.is_empty()


# 2. Reverse a String using Stack
def reverse_string(s: str) -> str:
    st = Stack()
    for ch in s:
        st.push(ch)
    out = []
    while not st.is_empty():
        out.append(st.pop())
    return "".join(out)


# 3. Postfix to Prefix
def postfix_to_prefix(postfix: str) -> str:
    st = Stack()
    operators = set(['+','-','*','/','^'])
    for ch in postfix.split():
        if ch not in operators:
            st.push(ch)
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.push(ch + " " + op2 + " " + op1)
    return st.pop()


# 4. Two stacks in an array
class TwoStacks:
    def __init__(self, n: int):
        self.arr = [None]*n
        self.size = n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.top1 + 1 == self.top2:
            raise IndexError("Stack1 Overflow")
        self.top1 += 1
        self.arr[self.top1] = x

    def push2(self, x):
        if self.top1 + 1 == self.top2:
            raise IndexError("Stack2 Overflow")
        self.top2 -= 1
        self.arr[self.top2] = x

    def pop1(self):
        if self.top1 < 0:
            return None
        v = self.arr[self.top1]
        self.top1 -= 1
        return v

    def pop2(self):
        if self.top2 >= self.size:
            return None
        v = self.arr[self.top2]
        self.top2 += 1
        return v


# 5. Delete Middle element from Stack
def delete_middle(st: Stack) -> None:
    def helper(s, current, size):
        if current == size // 2:
            s.pop()
            return
        val = s.pop()
        helper(s, current+1, size)
        s.push(val)
    helper(st, 0, len(st))


# 6. Reverse individual words in a sentence
def reverse_words(sentence: str) -> str:
    return " ".join(word[::-1] for word in sentence.split())


# 7. Valid Stack Permutation
def is_valid_stack_permutation(push_seq: List[int], pop_seq: List[int]) -> bool:
    st = []
    j = 0
    for x in push_seq:
        st.append(x)
        while st and j < len(pop_seq) and st[-1] == pop_seq[j]:
            st.pop()
            j += 1
    return j == len(pop_seq)


# 8. Stack with getMin() in O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


# 9. Stack with getRandom() in O(1)
class RandomStack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop() if self.data else None

    def get_random(self):
        if not self.data:
            return None
        return random.choice(self.data)


# 10. Equivalent expressions (infix equivalence via postfix)
def infix_to_postfix(expr: str) -> str:
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    st = Stack()
    output = []
    for ch in expr:
        if ch.isalnum():
            output.append(ch)
        elif ch == '(':
            st.push(ch)
        elif ch == ')':
            while not st.is_empty() and st.peek() != '(':
                output.append(st.pop())
            st.pop()
        else:
            while not st.is_empty() and st.peek() != '(' and prec.get(ch,0) <= prec.get(st.peek(),0):
                output.append(st.pop())
            st.push(ch)
    while not st.is_empty():
        output.append(st.pop())
    return "".join(output)

def equivalent_expressions(a: str, b: str) -> bool:
    return infix_to_postfix(a) == infix_to_postfix(b)


# 11. k stacks in a single array
class KStacks:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.arr = [None]*n
        self.top = [-1]*k
        self.next = list(range(1,n)) + [-1]
        self.free = 0

    def push(self, sn, val):
        if self.free == -1:
            raise IndexError("Stack Overflow")
        idx = self.free
        self.free = self.next[idx]
        self.arr[idx] = val
        self.next[idx] = self.top[sn]
        self.top[sn] = idx

    def pop(self, sn):
        if self.top[sn] == -1:
            return None
        idx = self.top[sn]
        self.top[sn] = self.next[idx]
        val = self.arr[idx]
        self.next[idx] = self.free
        self.free = idx
        return val


# 12. Largest Rectangle in Histogram
def largest_rectangle_area(heights: List[int]) -> int:
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, H * width)
        stack.append(i)
    return max_area


# 13. Clone a Stack without Extra Space (using recursion)
def clone_stack(orig: Stack) -> Stack:
    def insert_at_bottom(st, val):
        if st.is_empty():
            st.push(val)
        else:
            temp = st.pop()
            insert_at_bottom(st, val)
            st.push(temp)

    def clone_helper(st, cloned):
        if st.is_empty():
            return
        temp = st.pop()
        clone_helper(st, cloned)
        st.push(temp)
        insert_at_bottom(cloned, temp)

    cloned = Stack()
    clone_helper(orig, cloned)
    return cloned


# 14. Custom Browser History (using stack)
class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = homepage

    def visit(self, url: str):
        self.back_stack.push(self.current)
        self.current = url
        self.forward_stack = Stack()

    def back(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current)
            self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current)
            self.current = self.forward_stack.pop()
        return self.current


# 15. Maximum Rectangle with all 1s (matrix)
def max_rectangle_with_all_1s(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    max_area = 0
    heights = [0]*len(matrix[0])
    for row in matrix:
        for i,val in enumerate(row):
            heights[i] = heights[i]+1 if val==1 else 0
        max_area = max(max_area, largest_rectangle_area(heights))
    return max_area


# 16. Sort Stack using Recursion
def sort_stack(st: Stack):
    def insert_sorted(st, val):
        if st.is_empty() or val > st.peek():
            st.push(val)
        else:
            temp = st.pop()
            insert_sorted(st, val)
            st.push(temp)

    if not st.is_empty():
        temp = st.pop()
        sort_stack(st)
        insert_sorted(st, temp)


# 17. Stack with findMiddle() and deleteMiddle()
class MiddleStack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    def find_middle(self):
        n = len(self.stack)
        return self.stack[n//2] if n>0 else None
    def delete_middle(self):
        n = len(self.stack)
        if n>0:
            self.stack.pop(n//2)


# 18. Maximum visible people (next greater to right)
def max_visible_people(heights: List[int]) -> List[int]:
    """Return count of visible for each index — simplistic next greater example."""
    n = len(heights)
    ans = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if heights[j] >= heights[i]:
                ans[i]+=1
                break
            ans[i]+=1
    return ans


# 19. Count distinct Max Differences in Subarrays
def count_max_diff_subarrays(arr: List[int]) -> int:
    """Count distinct differences maximum for subarrays"""
    diffs = set()
    for i in range(len(arr)):
        mx = arr[i]
        for j in range(i, len(arr)):
            mx = max(mx, arr[j])
            diffs.add(mx - min(arr[i:j+1]))
    return len(diffs)


# 20. Longest Correct Bracket Subsequence Set
def longest_valid_brackets(s: str) -> int:
    stack = [-1]
    ans = 0
    for i,ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])
    return ans


# 21. Maximum of minimum for every window size
def max_of_min_for_every_window(arr: List[int]) -> List[int]:
    n = len(arr)
    stack = []
    left = [-1]*n
    right = [n]*n
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)
    ans = [0]*(n+1)
    for i in range(n):
        length = right[i]-left[i]-1
        ans[length] = max(ans[length], arr[i])
    for i in range(n-1,0,-1):
        ans[i] = max(ans[i], ans[i+1])
    return ans[1:]
