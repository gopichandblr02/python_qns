class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

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
print(count_nodes(root_obj))   # 3

# 10
# 20
# 30