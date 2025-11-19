class Solution:
    def max_sum(self, nums):
        max_sum = float('-inf')
        curr_sum = nums[0]
        for x in nums:
            curr_sum = max(x, x + curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def max_product(self,nums):
        min_prod=float('inf')
        max_prod=float('-inf')
        res=nums[0]
        for i,x in enumerate(nums):
            if x<0:
                min_prod,max_prod=max_prod,min_prod
            min_prod=min(x,x*min_prod)
            max_prod=max(x,x*max_prod)
            res=max(res,max_prod)
        return res

    def maxProfit(self,arr):
        min_profit = float('inf')
        max_profit = 0
        for x in arr[1:]:
            if x<min_profit:
                min_profit=x
            if x-min_profit> max_profit:
                max_profit=x-min_profit
        return max_profit

sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum
# print(sol.max_sum(nums))

print(sol.max_product([2, 3, -2, 4]))



arr=[7,1,5,3,6,4]

# print(sol.maxProfit(arr))