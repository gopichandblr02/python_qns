class Solution:
    def summaryRanges(self, nums):
        res=[]
        i=0
        x=len(nums)
        while i<x:
            start=i
            while i+1<x and nums[i]+1==nums[i+1]:
                i+=1
            end=i
            if nums[start] == nums[end]:
                res.append(str(nums[start]))
            else:
                res.append(f"{nums[start]}->{nums[end]}")
            i += 1
        return res


nums = [0,1,2,4,5,7]
sol=Solution()
print(sol.summaryRanges(nums))
# Output: ["0->2","4->5","7"]

nums1 = [0,2,3,4,6,8,9]
print(sol.summaryRanges(nums1))
# Output: ["0","2->4","6","8->9"]