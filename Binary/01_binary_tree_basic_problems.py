# ✅ 1. Binary Tree Node Definition (Used in All Problems)
"""

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ✅ 2. Count Nodes in a Binary Tree
def count_nodes(root):
    if not root:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)

root_obj = TreeNode(10)
root_obj.left = TreeNode(20)
root_obj.right = TreeNode(30)
print(root_obj.val)
print(root_obj.left.val)
print(root_obj.right.val)
# 10
# 20
# 30
print(count_nodes(root_obj))   # 3

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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# root.right.right = TreeNode(6)
print("Height of the tree:", height(root))  # Output: Height of the tree: 3

# ✅ 4. Diameter of Binary Tree
# (Number of nodes on the longest path between any two nodes)
"""
        1
       / \
      2   3
     / \
    4   5
4 → 2 → 5   (or 4 → 2 → 1 → 3)
Diameter = 3 (edges)

🔹 Key Insight (Interview Gold ✨)
At every node:
diameter = left_height + right_height
"""
# Short answer: it’s a nested function, not a closure
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


################################################################################################
########################################## Few More ############################################
################################################################################################

# 🌳 Binary Tree – Basics
# Node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1️⃣ Traversals (MOST IMPORTANT)
# Inorder (Left → Root → Right)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Preorder (Root → Left → Right)
def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

# Postorder (Left → Right → Root)
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

# 2️⃣ Maximum Depth of Binary Tree (LeetCode 104)
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


"""Time: O(n)
Space: O(h) (tree height)"""

# 3️⃣ Count Number of Nodes
def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

# 4️⃣ Sum of All Nodes
def sumNodes(root):
    if not root:
        return 0
    return root.val + sumNodes(root.left) + sumNodes(root.right)

# 5️⃣ Search a Value in Binary Tree
def search(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return search(root.left, target) or search(root.right, target)

# 6️⃣ Check if Two Trees Are Identical (LeetCode 100)
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (
        p.val == q.val and
        isSameTree(p.left, q.left) and
        isSameTree(p.right, q.right)
    )

# 7️⃣ Invert Binary Tree (LeetCode 226)
def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

# 8️⃣ Check if Tree is Symmetric (LeetCode 101)
def isSymmetric(root):
    def mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (
            t1.val == t2.val and
            mirror(t1.left, t2.right) and
            mirror(t1.right, t2.left)
        )

    return mirror(root.left, root.right)

# 9️⃣ Leaf Node Count
def countLeaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)

# 🔟 Height Balanced Tree (LeetCode 110)
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

"""
🧠 Very Important Patterns to Remember
Problem Type	Pattern
Height / Depth	Recursion
Traversal	DFS
Level Order	Queue (BFS)
Compare Trees	Recursive pair check
Invert / Mirror	Swap children
"""


print("*************")

class RootNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val,end=" ")
    in_order(root.right)

def pre_order(root):
    if not root:
        return
    print(root.val,end=" ")
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val,end=" ")


# Tree structure:
#       2
#      / \
#     3   4

root = RootNode(2)
root.left = RootNode(3)
root.right = RootNode(4)
in_order(root)
print("\n")
pre_order(root)
print("\n")
post_order(root)
# print(root)
# print(root.val,root.left,root.right)

