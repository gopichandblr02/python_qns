"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater
than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
"""

# index:   -1   0   1   2   ...  n-1   n
# value:  -∞   a   b   c        z    -∞


class Solution:
    def findPeakElement(self, nums):
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left

print(Solution().findPeakElement([1,2,3,1]))
# 2
print(Solution().findPeakElement([1,2,1,3,5,6,4]))
# 1 or 5
