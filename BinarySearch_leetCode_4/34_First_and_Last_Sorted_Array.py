"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    # 🎯 Goal
                    # We already found target at mid,
                    # but we don’t know if this is the first one.
                    right = mid - 1  # keep searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        def findLast():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1  # keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        return [findFirst(), findLast()]


sol=Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))  #Output: [3,4]
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))  #Output: [-1,-1]
print(sol.searchRange(nums = [], target = 0))  # Output: [-1,-1]
