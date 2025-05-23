# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, d):
            if not node: return None, d
            left = dfs(node.left, d+1)
            right = dfs(node.right, d+1)
            if left[1]==right[1]:
                return node, left[1]
            elif left[1]<right[1]:
                return right
            else:
                return left
        
        return dfs(root, 0)[0]
