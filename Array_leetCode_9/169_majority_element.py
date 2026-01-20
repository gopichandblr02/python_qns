nums = [2,2,1,1,1,2,2]


class Solution:

    # presence of an element increases count
    # Any other element will which has greater count will decrease existing elements count
    # Works on the logic - majority element always exists
    # ✔ Time: O(n)
    # ✔ Space: O(1)
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

    # ✔ Time: O(n)
    # ❌ Space: O(n)
    def majority_Element(self, nums):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > len(nums) // 2:
                return n


print(Solution().majorityElement([3,3,2]))
print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement(nums))

print(Solution().majority_Element([3,3,2]))
print(Solution().majority_Element([3,2,3]))
print(Solution().majority_Element(nums))