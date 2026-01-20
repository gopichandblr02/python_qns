# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))


# Input
root = [3, 9, 20, None, None, 15, 7]

# Output: 3

# Input
root = [1,None,2]
# Output: 2