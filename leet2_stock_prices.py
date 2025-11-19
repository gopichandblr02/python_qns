class Solution:
    def maxProfit(self,prices):
        if len(prices)<2:
            return 0
        min_price=float('inf')
        max_profit=0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

arr=[7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(arr))