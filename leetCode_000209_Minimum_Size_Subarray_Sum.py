class Solution:
    def mySol(self, target, nums):
        final_len = float('inf')
        for i,x in enumerate(nums):
            result,end=nums[i],i+1
            if result>=target:
                return 1
            while end<=len(nums)+1:
                result = sum(nums[i:end+1])
                if result >= target:
                    final_len = min(final_len, end-i+1)
                end+=1
        return final_len if final_len != float('inf') else 0

    def minSubArrayLen(self,tar,nums):
        left=0
        cur_sum=0
        min_len=float('inf')

        for right in range(len(nums)):
            cur_sum=cur_sum+nums[right]
            while cur_sum>=tar:
                min_len=min(min_len,right-left+1)
                cur_sum=cur_sum-nums[left]
                left+=1
        return min_len if min_len!=float('inf') else 0



print(Solution().minSubArrayLen(4, [1, 4, 4]))
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))

# 1
# 2
# 0