"""
Given an array of integers citations where citations[i] is the number of citations a researcher
received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such
that the given researcher has published at least h papers that have each been cited at least h times.
"""
class Solution:
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        for i in range(n):
            h = n - i
            if citations[i] >= h:
                return h
        return 0
sol=Solution()
print(sol.hIndex(citations = [3,0,6,1,5])) #
print(sol.hIndex(citations = [1,3,1])) # 1

"""
citations = [3,0,6,1,5]
sorted    = [0,1,3,5,6]
n = 5
"""
"""
| i | citations[i] | papers ≥ | condition | h     |
| - | ------------ | -------- | --------- | ----- |
| 0 | 0            | 5        | 0 ≥ 5 ❌   |       |
| 1 | 1            | 4        | 1 ≥ 4 ❌   |       |
| 2 | 3            | 3        | 3 ≥ 3 ✅   | **3** |
"""