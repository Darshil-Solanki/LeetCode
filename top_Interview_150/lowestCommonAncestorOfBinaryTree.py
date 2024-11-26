# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root or root == p or root==q:
                return root
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            if l and r:
                return root
            if not l:
                return r
            return l
        return dfs(root, p, q) 
