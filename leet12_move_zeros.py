class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # This didnt work ??

        return [x for x in nums if x>0]+[0]*(nums.count(0))

    def moveZeros_way2(self, nums):
        non_zero=0
        for i,x in enumerate(nums):
            if x!=0:
                nums[non_zero],nums[i]=nums[i],nums[non_zero]
                non_zero+=1
        return nums


sol=Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print(sol.moveZeros_way2([0,1,0,3,12]))
