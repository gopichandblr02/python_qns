class Solution:
    def maxProfit(self,prices):
        if len(prices)<2:
            return 0
        min_val=float('inf')
        max_profit=0
        for x in prices:
            if x<min_val:
                min_val=x
            elif max_profit < x-min_val:
                max_profit=x-min_val
        return max_profit

arr=[7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(arr))