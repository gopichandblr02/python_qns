# ✅ 1. Binary Tree Node Definition (Used in All Problems)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ✅ 2. Count Nodes in a Binary Tree

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

"""
      1
     / \
    2   3

Call flow:

count_nodes(1)
→ returns 1 + count_nodes(2) + count_nodes(3)

count_nodes(2)
→ returns 1 + count_nodes(None) + count_nodes(None) = 1

count_nodes(3)
→ returns 1 + count_nodes(None) + count_nodes(None) = 1
"""

# Return the height (max depth) of a binary tree.
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# ✅ 4. Diameter of Binary Tree
# (Number of nodes on the longest path between any two nodes)

def diameter(root):
    diameter_val = [0]

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        # path through this node
        diameter_val[0] = max(diameter_val[0], left + right)

        return 1 + max(left, right)

    dfs(root)
    return diameter_val[0]
