"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m,n=len(matrix),len(matrix[0])
        left,right=0,m*n-1
        while left<=right:
            mid = (left+right)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                left=mid+1
            else:
                right=mid-1
        return False

sol=Solution()
print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))

# Time Complexity: O(log(m * n)) where m is the number of rows and n is the number of columns.
# Space Complexity: O(1)
# why space complexity is O(1): The algorithm uses a constant amount of extra space regardless of the input size,
#  as it only uses a few variables for indexing and does not allocate additional data structures that grow with input size.