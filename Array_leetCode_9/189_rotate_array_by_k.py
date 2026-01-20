class Solution:
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k
    """
    Total time = O(k) + O(n−k) + O(n) = O(n)
    creates a brand-new list that contains all n elements, so additional space is:
    O(n) extra space.
    Even though slicing looks simple, Python must copy elements, so it is not in-place.
    """
    def rotate(self):
        self.k%=len(self.arr)  # To handle k>n
        return self.arr[-self.k:]+self.arr[:-self.k]

    """
    ✅ Rotate Array_leetCode_9 — Optimal In-Place Solution
    ✔ Time: O(n)
    ✔ Space: O(1) (no extra array)
    If LeetCode asks for O(1) extra space, you must use the reverse method instead.
    """
    def rotate_new(self):
        nums,k=self.arr,self.k
        k %= len(nums) # To handle k > n
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 1. Reverse entire array
        reverse(0, len(nums) - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest
        reverse(k, len(nums) - 1)
        return nums


arr=[1,2,3,4,5,6,7,8]
k=3
sol = Solution(arr,k)
print(sol.rotate())
print(sol.rotate_new())
# Steps
"""
12345(k=2)
54321
45321
45123
"""



