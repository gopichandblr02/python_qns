"""
What is a Height-Balanced Binary Tree?
A binary tree is height-balanced if for every node:
|height(left subtree) − height(right subtree)| ≤ 1

⚠️ Important:
This condition must hold at every node, not just the root.
"""
###########
"""
Height definition (LeetCode standard)
Height = number of edges on the longest downward path
None → height = 0
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isBalanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1

# Example usage:
# Constructing a balanced binary tree:
#         1
#        / \
#       2   3
#      / \  \
#     4    5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print(isBalanced(root))  # Output: True
# Constructing an unbalanced binary tree:
#         1
#        / \
#       2   3
#      /
#     4
#    /
#   5

root_unbalanced = TreeNode(1)
root_unbalanced.left = TreeNode(2)
root_unbalanced.right = TreeNode(3)
root_unbalanced.left.left = TreeNode(4)
root_unbalanced.left.left.left = TreeNode(5)
print(isBalanced(root_unbalanced))  # Output: False
