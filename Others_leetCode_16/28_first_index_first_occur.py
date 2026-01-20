"""
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "leetcode", needle = "leeto"
"""

class Solution():
    def func(self,strs,needle):
        strs_len, needle_len=len(strs),len(needle)
        if needle_len == 0:
            return 0
        for i in range(strs_len-needle_len+1):
            if strs[i:i+needle_len]==needle:
                return i
        else:
            return -1

haystack,needle = "sadbutsad","sad"
print(Solution().func(haystack,needle))