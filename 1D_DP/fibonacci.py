def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
# ⏱ Complexity
# Time: O(2ⁿ) ❌
# Space: O(n) (call stack)

# 2️⃣ Recursion + Memoization (Top-Down DP)
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
# ⏱ Complexity
# Time: O(n)
# Space: O(n)

# 3️⃣ Bottom-Up DP (Tabulation)
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# ⏱ Complexity
# Time: O(n)
# Space: O(n)


# 4️⃣ Space-Optimized DP (Most Common Interview Answer ⭐)
def fib_2(n):
    if n <= 1:
        return n
    prev1, prev2 = 0, 1
    curr=0
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev1, prev2 = prev2, curr
    return curr
# Time: O(n)
# Space: O(1) ✅
# 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34
print(fib_2(3))  # 2
print(fib_2(4))  # 3