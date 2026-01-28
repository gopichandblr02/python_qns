class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev1 = 1  # ways to reach step 1
        prev2 = 2  # ways to reach step 2
        curr=0
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(f"Number of ways to climb {n} stairs: {solution.climbStairs(n)}")  #8