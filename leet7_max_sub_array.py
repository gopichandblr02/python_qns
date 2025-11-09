class Solution:
    def maxSubArray(self, nums):
        max_sum=curr_sum=nums[0]
        for x in nums[1:]:
            curr_sum = max(x,curr_sum+x)
            max_sum = max(max_sum,curr_sum)
        return max_sum
    # Second with a different loop
    def maxSubArray111(self, nums):
        max_sum=curr_sum=nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum+nums[i])
            max_sum = max(max_sum,curr_sum)
        return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(sol.maxSubArray(arr))
print(sol.maxSubArray111(arr))