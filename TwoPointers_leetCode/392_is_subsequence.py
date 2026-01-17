# Two pointer approach

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)

print(Solution().isSubsequence("abc","ahbgdc"))
print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))

"""
| Approach    | Time           | Space |
| ----------- | -------------- | ----- |
| Two-pointer | O(n + m)       | O(1)  |
| Iterator    | O(n × m) worst | O(1)  |
"""

