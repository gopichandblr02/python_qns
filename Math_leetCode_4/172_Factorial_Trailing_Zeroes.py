"""
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n>0:
            n//=5
            count+=n
        return count
sol=Solution()
print(sol.trailingZeroes(n = 3)) # Output: 0
# Explanation: 3! = 6, no trailing zero.

print(sol.trailingZeroes(n = 5)) # Output: 1
# Explanation: 5! = 120, one trailing zero.
print(sol.trailingZeroes(n = 0)) # Output: 0

"""
In n!, there are way more 2s than 5s, so the number of trailing zeroes is determined by how many times 5 appears as a factor.
Every multiple of:
5 contributes at least one 5
25 = 5² contributes an extra 5
125 = 5³ contributes another extra 5
and so on…
"""
# n//5 + n//25 + n//125 + ...

# ⏱ Time & Space Complexity
"""
O(log₅ n)
O(1)
"""
