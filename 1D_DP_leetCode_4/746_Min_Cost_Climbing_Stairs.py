"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        prev1=cost[0]
        prev2=cost[1]
        n=len(cost)
        for i in range(2,n):
            curr=cost[i]+min(prev1,prev2)    # We are calculating current step cost
            prev1=prev2
            prev2=curr
        return min(prev1,prev2)               # Return min of current step and previous step


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    cost = [10, 15, 20]
    print(f"Minimum cost to climb stairs: {solution.minCostClimbingStairs(cost)}") #15
    print(f"Minimum cost to climb stairs: {solution.minCostClimbingStairs([10,15,20,100])}") #30