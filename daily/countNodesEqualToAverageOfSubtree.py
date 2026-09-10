# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0 # ans, sum, no

            left = dfs(node.left)
            right = dfs(node.right)

            tot = node.val + left[1] + right[1]
            cnt = 1 + left[2] + right[2]
            ans = left[0] + right[0] + (1 if node.val == tot//cnt else 0)
            
            return ans, tot, cnt

        
        return dfs(root)[0]
