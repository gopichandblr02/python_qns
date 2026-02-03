"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""
class Solution:
    # Not recommended
    def native(self,x: float, n: int):
        res = 1
        for _ in range(n):
            res *= x

    # ✅ Iterative Solution(Best for interviews)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:   # n is odd
                result *= x
            x *= x           # Square base element
            n//=2              # or n=n//2   # Half exponent
        return result

"""
| Metric    | Value        |
| --------- | ------------ |
| **Time**  | **O(log n)** |
| **Space** | **O(1)**     |
"""

sol=Solution()
print(sol.myPow(x = 2.00000, n = 10)) # Output: 1024.00000
print(sol.myPow(x = 2.10000, n = 3)) # Output: 9.26100
print(sol.myPow(x = 2.00000, n = -2)) # Output: 0.25000