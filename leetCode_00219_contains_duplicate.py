class Solution:
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        hashMap={}
        for i,x in enumerate(nums):
            if x in hashMap:
                if abs(hashMap[x]-i)<=k:
                    return True
            hashMap[x]=i
        else:
            return False

    def containsNearbyDuplicate2(nums, k):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

# ✅ Sliding Window (Set) – Best & Clean
#
# Keeps only k elements in memory.
#
# Time: O(n)
# Space: O(k)

    def containsNearbyDuplicate3(nums, k):
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
        return False
