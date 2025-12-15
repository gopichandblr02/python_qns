class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap={}
        for i,x in enumerate(nums):
            if x in hashMap:
                if abs(hashMap[x]-i)<=k:
                    return True
            hashMap[x]=i
        else:
            return False