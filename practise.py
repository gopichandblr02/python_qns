class Solution:
    def maxProfit(self,arr):
        min_profit = float('inf')
        max_profit = 0
        for x in arr[1:]:
            if x<min_profit:
                min_profit=x
            if x-min_profit> max_profit:
                max_profit=x-min_profit
        return max_profit





arr=[7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(arr))