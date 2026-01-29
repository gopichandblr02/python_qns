# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

# Input
root = [3, 9, 20, None, None, 15, 7]
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
solution = Solution()
print(solution.maxDepth(tree))
# Output: 3

# Input
root1 = [1,None,2]
tree1 = TreeNode(1)
tree1.right = TreeNode(2)
solution = Solution()
print(solution.maxDepth(tree1))
# Output: 2