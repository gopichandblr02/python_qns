class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            rem = target-num
            if rem in seen:
                return [seen[rem],i]
            else:
                seen[num]=i

    def twoSum2(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            rem = target-num
            if rem in seen:
                return [seen[rem],i]
            seen[num]=i  # Just to show that it works without else as well

sol = Solution()
print(sol.twoSum([3,2,4],6))