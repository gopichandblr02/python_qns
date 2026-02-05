"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums) -> bool:
        prevMaxReach = 0
        for i in range(len(nums)):
            if i > prevMaxReach:
                return False
            prevMaxReach = max(prevMaxReach, i + nums[i])
        return True

# ⏱ Complexity
# Time: O(n)
# Space: O(1)

sol=Solution()
print(sol.canJump([2,3,1,1,4]))
# Output: true
print(sol.canJump([3,2,1,0,4]))
# Output: false

"""
| i | nums[i] | maxReach       |
| - | ------- | -------------- |
| 0 | 3       | 3              |
| 1 | 2       | 3              |
| 2 | 1       | 3              |
| 3 | 0       | 3              |
| 4 | 4       | ❌ cannot reach |

"""