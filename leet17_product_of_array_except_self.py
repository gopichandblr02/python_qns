nums =[1,2,3,4]
nums2=[5,1,3]
class Solution:
    def productExceptSelf(self,nums):
        nums_len = len(nums)
        ans = [1]*nums_len
        prefix=1
        for i in range(nums_len):
            ans[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(nums_len-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans
    def using_div(self,nums):
        total_product = 1
        zero_count = nums.count(0)
        # Case 1: More than one zero → all products will be zero
        if zero_count > 1:
            return [0] * len(nums)
        # Case 2: One zero → only the index with zero gets the product of non-zero elements
        if zero_count == 1:
            product_non_zero = 1
            for x in nums:
                if x != 0:
                    product_non_zero *= x
            result = [0] * len(nums)
            result[nums.index(0)] = product_non_zero
            return result
        # Case 3: No zeros → normal division
        for x in nums:
            total_product *= x
        return [total_product // x for x in nums]


print(Solution().productExceptSelf(nums))
print(Solution().productExceptSelf(nums2))

print(Solution().using_div(nums))
print(Solution().using_div(nums2))