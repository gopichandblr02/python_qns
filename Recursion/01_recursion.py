# Recursion is when a function calls itself to solve a smaller part of the same problem
# until a stopping condition called a base case is reached.

# def function():
#     if base_condition:
#         return something  # base case
#     return function(smaller_problem)  # recursive case

# 1. Example: Factorial (Classic Recursion)
# n! = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    if n == 0 or n == 1:     # base case
        return 1             # Recursion ends here.....when it reaches base case...no loop needed
    return n * factorial(n - 1)   # recursive call
print(factorial(5))  # 120

# Fibonacci numbers:
# 0, 1, 1, 2, 3, 5, 8 ...

def fib(n):
    if n <= 1:      # base case
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))   # 8

# Sum of Digits of a Number
# 123 → 1 + 2 + 3 = 6
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(123))  # 6

# Reverse a String (Recursion)
def reverse_string(s):
    if len(s) == 0:     # base case
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # "olleh"

# Example: sum all elements
def list_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + list_sum(arr[1:])

print(list_sum([1, 2, 3, 4]))  # 10

# Recursion is heavily used in tree problems.
# Example: Count nodes in a binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_nodes(root):
    if not root:           # base case
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Example tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(count_nodes(root))  # 3

# 🔹 7. Recursion in Backtracking: Generate All Subsets
def subsets(nums):
    result = []

    def backtrack(i, path):
        if i == len(nums):
            result.append(path)
            return

        # include nums[i]
        backtrack(i + 1, path + [nums[i]])
        # exclude nums[i]
        backtrack(i + 1, path)

    backtrack(0, [])
    return result
print(subsets([1, 2, 3]))

"""
| Problem          | Base Case    | Recursive Step                    |
| ---------------- | ------------ | --------------------------------- |
| Factorial        | n == 0       | n * factorial(n-1)                |
| Fibonacci        | n ≤ 1        | fib(n-1) + fib(n-2)               |
| Sum of digits    | n == 0       | last digit + sum_of_digits(n//10) |
| Reverse string   | len == 0     | reverse rest + first char         |
| List sum         | len == 0     | arr[0] + list_sum(rest)           |
| Count tree nodes | root is None | count left + right                |
"""

##### **** Tail Recursion ***  #####

# Python doesnt support.....read more on this

"""
Tail recursion optimization (TRO) — often called tail-call optimization (TCO) — is a compiler/VM optimization that lets 
a recursive function call itself without growing the call stack, but only when the recursive call is in tail position.
"""


def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_factorial(n - 1, acc * n)  # tail position

# Here, nothing happens after the recursive call.
# So in languages that support tail-call optimization, the compiler can replace the call with a loop internally.