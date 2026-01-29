"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums):
        nums_len=len(nums)
        if nums_len==0:
            return None
        if nums_len==1:
            return nums[0]
        prev1=nums[0]
        prev2=max(nums[0],nums[1])
        for i in range(2,nums_len):
            cur_max=max(prev2,nums[i]+prev1)
            prev1=prev2
            prev2=cur_max
        return prev2

nums = [1, 2, 3, 1]
sol=Solution()
print(sol.rob(nums))
# Output: 4
print(sol.rob([1,1]))
# Output: 1
print(sol.rob([0]))
# Output: 0