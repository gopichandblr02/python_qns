"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i.
 In other words, if you are at index i, you can jump to any index (i + j) where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
"""
class Solution:
    def jump(self, nums) -> int:
        cur_max=0
        prev_max=0
        jumps=0
        for i in range(len(nums)-1):
            cur_max=max(cur_max,i+nums[i])
            if i==prev_max:
                jumps+=1
                prev_max=cur_max
        return jumps

sol=Solution()
print(sol.jump(nums = [14,3,1,1,4]))
# Output: 1
print(sol.jump(nums = [2,3,1,1,4]))
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
print(sol.jump(nums = [2,3,0,1,4]))
# Output: 2