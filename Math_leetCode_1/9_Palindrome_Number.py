class Solution:
    #my sol
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            st = str(x)
            i=0
            end=len(st)
            check=(len(st)//2)-1
            while i <=check:
                if st[i]==st[end-i-1]:
                    i+=1
                elif st[i]!=st[end-i-1]:
                    return False
            return True

    # Complexity
    # Time: O(n)
    # Space: O(n)
    def isPalindrome1(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    # Time: O(log₁₀ n) → number of digits
    # Space: O(1) → constant extra space ✅
    def isPalindrome2(self, x: int) -> bool:
        # Edge cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits:  x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
# Explanation for time complexity
"""
| x value | digits left |
| ------- | ----------- |
| 12345   | 5           |
| 1234    | 4           |
| 123     | 3           |
| 12      | 2           |
| 1       | 1           |
| 0       | stop        |
"""
"""    Examples:
    n = 9 → 1     digit → log₁₀(9) ≈ 0.95
    n = 99 → 2    digits → log₁₀(99) ≈ 1.99
    n = 1000 → 4  digits → log₁₀(1000) = 3
     digits = ⌊log₁₀(n)⌋ + 1
     ≈ log₁₀(n) times
"""

print(Solution().isPalindrome(x = 121))
# Output: true
print(Solution().isPalindrome(x = -121))
# Output: false
print(Solution().isPalindrome(x = 10))
# Output: false