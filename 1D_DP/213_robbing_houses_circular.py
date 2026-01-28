class Solution:
    def rob(self, nums):
        nums_len=len(nums)
        if nums_len==0:
            return 0
        if nums_len<=2:
            return max(nums)
        def rob_inner(new_nums):
            prev1=new_nums[0]
            prev2=max(new_nums[0],new_nums[1])
            curr=prev2
            for i in range(2,len(new_nums)):
                curr=max(new_nums[i]+prev1,prev2)
                prev1=prev2
                prev2=curr
            return curr
        case1=rob_inner(nums[1:])
        case2=rob_inner(nums[:-1])
        return max(case1,case2)

sol=Solution()
print(sol.rob(nums = [2,3,2]))
# Output: 3
print(sol.rob([1,2,3,1]))
# Output: 4