"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time."""


class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        # first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # first col
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Rest
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[m - 1][n - 1]

sol=Solution()
print(sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])) # Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
print(sol.minPathSum(grid = [[1,2,3],[4,5,6]]))
# Output: 12

# ⏱️ Complexity
# Time: O(m × n)
# Space: O(1) (in-place DP)

"""
💡 Core Idea (Dynamic Programming)
At any cell (i, j), the cheapest way to get there must come from:
top (i-1, j) or
left (i, j-1)
"""
# dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
