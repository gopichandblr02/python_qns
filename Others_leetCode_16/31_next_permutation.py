# Input: arr[] = [2, 4, 1, 7, 5, 0]
# Output:      = [2, 4, 5, 0, 1, 7]

class Solution:
    def my_sol(self,nums):
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i + 1]:
            i-=1
        if i>=0:
            j=-1
            while nums[j] <= nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i + 1:])
        return nums

    def next_permutation(self,nums):
        n = len(nums)
        # 1. Find first decreasing index from the end
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2. Find element just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # 4. Reverse the remaining part
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums

# a = [1, 2, 3]
# print(next_permutation(a))
np=Solution()
print(np.next_permutation([2, 4, 1, 7, 5, 0]))   #[2, 4, 5, 0, 1, 7]
print(np.next_permutation([2, 4, 1, 5, 7, 0]))   #[2, 4, 1, 7, 0, 5]
print(np.next_permutation([2, 4, 1, 5, 7, 6]))   #[2, 4, 1, 6, 5, 7]
