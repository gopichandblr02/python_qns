class Solution:
    def func(self,strs):
        pref = strs[0]
        for x in strs[1:]:
            while not x.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return   # same as return None
        return pref


strs = ["flower","flow","flight"]
strs1 = ["flower","aa","cc"]
sol = Solution()
print(sol.func(strs)) # fl
print(sol.func(strs1)) # None

# ⏱ Time Complexity
"""Worst Case"""

# Each startswith(pref) comparison takes O(m) in worst case.
# Prefix may shrink from length m → 0, so at most m checks per string.

# So total work:
# n strings × m prefix reductions × m comparison
# = O(n · m²)


# But Python’s startswith() stops as soon as mismatch occurs, so in practice:

# Interview-accepted complexity:
"""
O(n · m)
Where:
n = number of strings
m = length of shortest string / prefix
"""

# Why interviewers say O(n·m)
# Because:
"""
Every character in each string is compared at most once while shrinking.
Total comparisons are bounded by total characters.
"""

# So:
# Total character comparisons ≤ n × m

# 🧠 FAANG-level explanation
"""
We start with the first string as the prefix and iteratively reduce it until it matches all other strings.
Each character of the prefix is removed at most once, and for each string we only compare characters until mismatch.
Therefore, the total number of character comparisons across all strings is bounded by O(n·m).
"""

# 📦 Space Complexity
# O(1)
# Only a variable pref is used. No extra data structures.

# Interview Notes (FAANG style)
"""
| Aspect           | Answer                           |
| ---------------- | -------------------------------- |
| Time Complexity  | **O(n·m)**                       |
| Space Complexity | **O(1)**                         |
| Approach         | Horizontal scanning              |
| Why efficient    | Prefix shrinks only, never grows |
| Best Case        | O(n)                             |
| Worst Case       | O(n·m)                           |
"""
