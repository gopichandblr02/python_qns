class Solution:
    def __init__(self,arr):
        self.arr = arr

    def max_product_subarray(self):
        max_prod=self.arr[0]
        min_prod =self.arr[0]
        result =self.arr[0]

        for i in range(1,len(self.arr)):
            if self.arr[i]<0:
                max_prod,min_prod=min_prod,max_prod
            max_prod=max(self.arr[i],self.arr[i]*max_prod)
            min_prod=min(self.arr[i],self.arr[i]*min_prod)
            result=max(result,max_prod)
        return result

nums = [2, 3, -2, 4]
sol = Solution(nums)
print(sol.max_product_subarray())  # Output: 6