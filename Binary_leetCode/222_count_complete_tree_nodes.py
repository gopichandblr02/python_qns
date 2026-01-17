# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:
#
# Input: root = []
# Output: 0
# Example 3:
#
# Input: root = [1]
# Output: 1
