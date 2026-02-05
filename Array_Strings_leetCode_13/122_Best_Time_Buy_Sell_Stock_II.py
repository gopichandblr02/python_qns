"""
prices = [1, 2, 3, 4]
profit = (2-1) + (3-2) + (4-3) = 3
"""

# ✅ Greedy Approach (Optimal)
"""
Algorithm
Iterate from day 1 to n-1
If prices[i] > prices[i-1], add the difference to profit
"""

# [1,1,0,4,100]


class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# Example usage:
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))  # Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit = 4 + 3 = 7.

# Example 2:
prices = [1, 2, 3, 4, 5]
solution = Solution()
print(solution.maxProfit(prices))  # Output: 4


##################################################################################################################
###################🔹 What is a Greedy Approach? #################################################################
##################################################################################################################

# A greedy approach means:
# 1. At every step, make the locally optimal choice, hoping it leads to a globally optimal solution.
# Key characteristics:
"""
Decisions are made step-by-step
No backtracking
No revisiting earlier choices
Simple and efficient (often O(n))
"""

# ⚠️ Important:
# Greedy does NOT work for all problems — it works only when the problem has the greedy-choice property.

# 🔹 Greedy Choice in Stock II (LC 122)
# The Greedy Rule:
"""
Take every profit whenever today’s price is higher than yesterday’s price
That is:
If prices[i] > prices[i-1]:
    take (prices[i] - prices[i-1])
"""

# 🔹 Why This Greedy Choice Works Here
# ✅ Key Property of the Problem

"""
You can buy & sell any number of times
You cannot hold multiple stocks
There is no transaction fee
There is no cooldown
"""

# These conditions make the problem perfect for greedy.
# 🔹 Core Insight (Very Important)
# Any profitable long transaction can be broken into multiple smaller profitable transactions without changing total profit.

# Example
# prices = [1, 3, 5]

"""
Option 1 (single transaction):
Buy at 1, Sell at 5 → Profit = 4
Option 2 (greedy transactions):
Buy at 1, Sell at 3 → +2
Buy at 3, Sell at 5 → +2
👉 Total = 4
Same profit ✅
"""

# 🔹 Mathematical Proof (Interview-Friendly)
# For increasing prices:
# prices = p0, p1, p2, p3

"""If:
p0 < p1 < p2 < p3
Then:
(p3 - p0) = (p1 - p0) + (p2 - p1) + (p3 - p2)"""

"""So:
Taking every increase is equivalent to taking the best buy/sell window
You never lose profit by selling earlier and rebuying"""

# 🔹 What About Price Drops?
# prices = [5, 3]

"""No profit possible:
Greedy skips it
Any transaction would lose money
So greedy avoids bad decisions naturally."""

# 🔹 Intuition in Plain English
# Think of it like hiking:
# Every uphill step → you gain height (profit)
# Downhill steps → ignore
# Total height gained = sum of all uphill climbs
# You don’t need to jump from the lowest valley to the highest peak.

# 🔹 Why Greedy Is Optimal (Formal Reason)
"""This problem satisfies:
✔ Greedy-Choice Property
Choosing local profit does not prevent reaching global maximum profit."""

# ✔ Optimal Substructure
"""Max profit up to day i depends only on max profit up to day i-1."""

# 🔹 Contrast With Problems Where Greedy FAILS
"""Greedy would NOT work if:
There was a transaction fee (LC 714)
There was a cooldown (LC 309)
Limited transactions (LC 123)
Those require DP, not greedy."""

# 🔹 One-Line Interview Answer 🚀
# Greedy works here because every increasing price segment can be split into independent profitable transactions,
# and summing all positive differences always equals the maximum possible profit.