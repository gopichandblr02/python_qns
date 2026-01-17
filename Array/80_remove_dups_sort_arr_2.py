class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return len(nums)
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i, nums

nums = [1,1,1,2,2,3]
sol=Solution()
print(sol.removeDuplicates(nums))
# Expected  [1,1,2,2,3]

nums1=[0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums1))
# Expected [0,0,1,1,2,3,3]

