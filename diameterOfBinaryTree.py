# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node: return 0
            return 1+max(height(node.left), height(node.right))

        def dfs_diameter(node):
            if not node: return 0
            diameter = height(node.left) + height(node.right)
            return max(diameter, dfs_diameter(node.left), dfs_diameter(node.right))
            
        return dfs_diameter(root)


        # both combined finding height and calculating max diameter
        # self.ans = 0

        # def dfs(node):
        #     if not node: return 0
        #     # height of tree
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     # diameter of tree
        #     self.ans = max(self.ans, left+right)
        #     return 1+max(left, right)
        
        # dfs(root)
        # return self.ans
