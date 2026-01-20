# ⭐ Optimal Solution — DFS (O(n) time)

def hasPathSum(root, targetSum):
    if not root:
        return False

    # If it's a leaf
    if not root.left and not root.right:
        return root.val == targetSum

    return (hasPathSum(root.left, targetSum - root.val) or
            hasPathSum(root.right, targetSum - root.val))
