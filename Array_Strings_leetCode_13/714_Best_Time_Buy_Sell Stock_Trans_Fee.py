class Solution:
    def maxProfit(self, prices, fee):
        profit = 0
        min_val = -prices[0]

        for price in prices[1:]:
            profit = max(profit, min_val + price - fee)
            min_val = max(min_val, profit - price)

        return profit

# Example usage:
prices = [1, 3, 2, 8, 4, 9]
fee = 2
solution = Solution()
print(solution.maxProfit(prices, fee))  # Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at price 1 and selling at price 8, profit = 8 - 1 - 2 = 5
# - Buying at price 4 and selling at price 9, profit = 9 - 4 - 2 = 3
# Total profit = 5 + 3 = 8

# Example usage:
prices = [1, 3, 7, 5, 10, 3]
fee = 3
solution = Solution()
print(solution.maxProfit(prices, fee))  # Output: 6


# def maxProfit(self, prices):
#     if len(prices) < 2:
#         return 0
#     min_price = float('inf')
#     max_profit = 0
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#     return max_profit