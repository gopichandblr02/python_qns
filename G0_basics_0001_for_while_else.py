# Below is a clear, interview-oriented explanation of:
"""
- for loop
- while loop
- (Python’s alternative to do-while)
- for-else
- while-else
"""

# 1️⃣ for loop
"""Used when the number of iterations is known or you are iterating over a collection.
Basic example"""

for i in range(3):
    print(i)
# Output
# 0
# 1
# 2

# Iterating over a list
nums = [10, 20, 30]
for n in nums:
    print(n)

# Edge cases
# 🔹 Empty iterable
for x in []:
    print(x)
print("Done")
# Output
#
# Done

# ✔ Loop body never executes
# 2️⃣ while loop
"""Used when iterations depend on a condition.
Basic example"""
i = 0
while i < 3:
    print(i)
    i += 1

# Edge cases
# 🔹 Condition false initially
i = 5
while i < 3:
    print(i)
print("Done")

# Output
#
# Done

# ✔ Body never executes
# 🔹 Infinite loop (common bug ⚠️)
i = 0
while i < 3:
    print(i)
    # i += 1  ❌ missing
# ✔ Runs forever

# 3️⃣ do-while loop (Not directly in Python ❌)
# Python does NOT have a native do-while loop.
# ✅ Python workaround (runs at least once)
i = 5
while True:
    print(i)
    i += 1
    if i > 7:
        break

# ✔ Executes at least once, even if condition is initially false.
# Edge case
i = 100
while True:
    print("Runs once")
    break

# 4️⃣ for-else loop ⭐ (VERY IMPORTANT)
# else runs only if loop completes normally
# ❌ else does NOT run if break is executed
# Example – Search element

nums = [1, 3, 5, 7]
target = 5

for n in nums:
    if n == target:
        print("Found")
        break
else:
    print("Not Found")


# Output
#
# Found
#
# When else runs
target = 9

for n in nums:
    if n == target:
        print("Found")
        break
else:
    print("Not Found")


# Output
#
# Not Found
#
# Edge case – Empty iterable
for x in []:
    print(x)
else:
    print("Else executed")


# ✔ else executes
# 5️⃣ while-else loop
# Same rule as for-else:
# else runs only if no break occurs
# Example
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop completed normally")


# Output
#
# 0
# 1
# 2

# Loop completed normally
# With break
i = 0
while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print("Completed")


# Output
#
# 0


# ✔ else skipped
# Edge case – Condition false initially
i = 5
while i < 3:
    print(i)
else:
    print("Else runs")


# ✔ else runs
# 🔥 Key Differences Summary
# Loop Type   	Runs At Least Once	Else Executes When
"""
| Loop Type              | Runs At Least Once | Else Executes When |
| ---------------------- | ------------------ | ------------------ |
| `for`                  | ❌                  | No `break`         |
| `while`                | ❌                  | No `break`         |
| `do-while` (simulated) | ✅                  | N/A                |
| `for-else`             | ❌                  | Loop finishes      |
| `while-else`           | ❌                  | Loop finishes      |
"""

# 💡 Real LeetCode / Interview Use Cases
# ✔ Detect prime using for-else
n = 7
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# ✔ Search problems

def func():
    arr = []
    for x in arr:
        if x == target:
            break
    else:
        return -1



######################################################################################
########################## LeetCode problems using for-else ##########################
######################################################################################


# Below are REAL LeetCode-style problems where for-else is clean, Pythonic, and interview-impressive.
# I’ll show problem idea → why for-else fits → code → edge cases.

# 🔹 1. Check if Number is Prime
# (Common interview warm-up)
# Idea
# If no divisor is found → number is prime
# Perfect fit for for-else.

# Code
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

# Why for-else?
# ✔ else runs only if loop never breaks (no divisor found)

# 🔹 2. Search an Element in Array
# (LeetCode 704 – Binary Search logic variant)
# Code

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    else:
        return -1

# Edge case
nums = []
target = 5
# loop skipped → else runs → -1

# 🔹 3. Check if All Characters Are Unique
# (LeetCode 387 style logic)

# Code
def allUnique(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    else:
        return True

# Why for-else?
# ✔ If no duplicate is found, loop finishes normally
# 🔹 4. Find First Duplicate in Array
# (Interview / LeetCode variant)
# Code
def firstDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    else:
        return -1

# 🔹 5. Valid Parentheses (Early Exit Case)
# (LeetCode 20)
# Code
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)
    else:
        return not stack

# Why for-else?
# ✔ else executes only if loop never failed early
# 🔹 6. Check If String Is Palindrome
# (LeetCode 125 – simplified)
# Code
def isPalindrome(s):
    s = s.lower()
    i, j = 0, len(s) - 1

    for _ in range(len(s) // 2):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    else:
        return True

# 🔹 7. Detect Cycle in Linked List (Naive version)
# (LeetCode 141 – educational)

def hasCycle(head):
    seen = set()
    curr = head

    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    else:
        return False

# 🔹 8. Word Break Check (Simplified version)
# (LeetCode 139 – concept demo)

def wordBreak(s, wordDict):
    for word in wordDict:
        if s.startswith(word):
            return True
    else:
        return False

# 🔥 Interview Tip (VERY IMPORTANT)

"""for-else is NOT “if-else”
else executes when no break happens"""

# Interview One-Liner:

""""I used for-else to handle the case where the loop completes without finding a match."""

# 🧠 When NOT to Use for-else

"""
❌ If logic is unclear
❌ If loop always returns
❌ If readability suffers
"""
