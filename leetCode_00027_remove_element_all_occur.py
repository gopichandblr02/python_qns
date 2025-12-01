"""
    Given an array nums and a value val, remove all instances of that value
    in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave
    beyond the new length.

    Example:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums
    being 2.
    It doesn't matter what you leave beyond the returned length.
"""

# Here if we use remove, it will re-index and we will miss a few elements


class Sol:
    def remove_element(self,nums,val):
        i=len(nums)-1
        while i>=0:
            if nums[i]==val:
                nums.pop(i)
            i-=1
        return nums,len(nums)

# print(Sol().remove_element([3,2,2,3],3))
print(Sol().remove_element([0,1,2,2,3,0,4,2],2))

# Remove vs pop in lists

"""
| Feature          | `remove()`           | `pop()`                                       |
| ---------------- | -------------------- | --------------------------------------------- |
| Removes by       | **value**            | **index**                                     |
| Returns          | **Nothing (`None`)** | **Removed element**                           |
| Errors if        | Value not found      | Index out of range                            |
| Default behavior | —                    | Removes **last element**                      |
| Time complexity  | **O(n)**             | **O(1)** for last element, **O(n)** otherwise |
| Mutates list?    | Yes                  | Yes                                           |
"""

