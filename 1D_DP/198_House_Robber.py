

class Solution:
    def rob(self, nums):
        nums_len=len(nums)
        if nums_len==0:
            return None
        if nums_len==1:
            return nums[0]
        prev1=nums[0]
        prev2=max(nums[0],nums[1])
        cur_max=prev2
        for i in range(2,nums_len):
            cur_max=max(prev2,nums[i]+prev1)
            prev1=prev2
            prev2=cur_max
        return cur_max

nums = [1, 2, 3, 1]
sol=Solution()
print(sol.rob(nums))
# Output: 4
print(sol.rob([1,1]))
# Output: 1
print(sol.rob([0]))
# Output: 0