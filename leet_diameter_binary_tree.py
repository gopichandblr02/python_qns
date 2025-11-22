class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # update global diameter
            self.diameter = max(self.diameter, left + right)

            # return height of subtree
            return 1 + max(left, right)

        dfs(root)
        return self.diameter


print(Solution().diameter())