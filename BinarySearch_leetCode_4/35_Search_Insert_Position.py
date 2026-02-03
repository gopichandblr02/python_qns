"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    # O(n)
    def searchInsert(self, nums, target):
        i=0
        nums_len=len(nums)
        while i<nums_len:
            if nums[i]>=target:
                return i
            i+=1
        return nums_len
    # O(log n)
    def searchInsertOptimized(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

"""
| Iteration | Remaining elements |
| --------- | ------------------ |
| 0         | n                  |
| 1         | n / 2              |
| 2         | n / 4              |
| 3         | n / 8              |
| k         | n / 2ᵏ             |
"""
# We stop when:
# n / 2ᵏ = 1

# 2ᵏ = n
# k = log₂(n)




sol=Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))
# 2
print(sol.searchInsert(nums = [1,3,5,6], target = 2))
# 1
print(sol.searchInsert(nums = [1,3,5,6], target = 7))
# 4
print('-------')
print(sol.searchInsertOptimized(nums = [1,3,5,6], target = 5))
# 2
print(sol.searchInsertOptimized(nums = [1,3,5,6], target = 2))
# 1
print(sol.searchInsertOptimized(nums = [1,3,5,6], target = 7))
# 4