class Solution:
    def longestConsecutive(self, nums):
        num_set=set(nums)
        result=0

        for x in num_set:
            length=0
            if x-1 not in num_set:
                current=x
                length=1
                while current+1 in num_set:
                    current+=1
                    length+=1
            result=max(result,length)
        return result








nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
sol=Solution()
print(sol.longestConsecutive(nums))

nums1 = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

nums3 = [1,0,1,2]
# Output: 3