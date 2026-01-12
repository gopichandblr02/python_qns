class Solution:
    def isSymmetric(self, root):
        if not root.left and not root.right:
            return True
        return root.left and root.right and self.isSymmetric(root.right) and self.isSymmetric(root.left)