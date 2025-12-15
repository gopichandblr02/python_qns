class Solution:
    def twoSum(self, numbers, target):
        hashMap={}
        for i,x in enumerate(numbers):
            rem=target-x
            if rem in hashMap:
                return [hashMap[rem],i+1]
            else:
                hashMap[x]=i+1

print(Solution().twoSum(numbers=[2,7,11,15], target = 9))
# Output: [1,2]
print(Solution().twoSum(numbers=[2,3,4], target = 6))
# Output: [1,3]