"""✅ LeetCode 209: Minimum Size Subarray Sum
Problem

Given an array nums of positive integers and an integer target,
return the minimum length of a contiguous subarray such that:
    Example:
    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2
"""

class Solution:
    def min_sum(self,nums,target=7):
        left = 0
        curr_sum = 0
        min_len = float('inf')
        for right in range(len(nums)):
            curr_sum += nums[right]
            # shrink window as long as sum >= target
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

print(Solution().min_sum([2,3,1,2,4,3],7))

"""
TIP:
| Operation  | Time Complexity | Space Complexity |
| ---------- | --------------- | ---------------- |
| `len(arr)` | **O(1)**        | **O(1)**         |
"""



