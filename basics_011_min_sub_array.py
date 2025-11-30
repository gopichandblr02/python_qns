"""
✅ Find the Minimum Sum Subarray (Contiguous)

Problem: Given an integer array nums, find the contiguous subarray with the minimum possible sum, and return that sum.

Example:
nums = [3, -4, 2, -3, -1, 7, -5]
Minimum sum subarray = [-4, 2, -3, -1] → sum = -6

"""
class Sol:
    def min_sub_arr(self,arr):
        arr_len=len(arr)
        min_sum=float('inf')
        cur_min=float('inf')
        for i in range(arr_len):
            min_sum=min(arr[i],min_sum+arr[i])
            cur_min=min(cur_min,min_sum)
        return cur_min

nums = [3, -4, 2, -3, -1, 7, -5]
print(Sol().min_sub_arr(nums))