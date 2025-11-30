#### What is a binary tree with example

A binary tree is a tree data structure where each node can have at most two children.
These children are usually called:
- Left child 
- Right child

It is one of the most common structures used in algorithms, recursion, searching, etc.

A binary tree is a hierarchical structure made of nodes, where:

1. Each node contains data
2. Each node can have 0, 1, or 2 children
3. The topmost node is called the root
4. An edge in a binary tree is the link or connection between a parent node and its child node

```
         10
        /  \
       5    15
      / \     \
     2   7     20
```

Explanation:
- 10 is the root
- 10 has two children → 5 (left) and 15 (right)
- 5 has two children → 2 and 7
- 15 has one child → 20
- 2, 7, and 20 are leaf nodes (no children)


```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

A Binary Search Tree (BST) is a special type of binary tree that follows a strict ordering rule:

✅ Definition of a BST

- A Binary Search Tree is a binary tree where every node satisfies:
- Left subtree values < node value
- Right subtree values > node value
- Both left and right subtrees must also be BSTs
- This makes searching efficient (O(log n) on average).