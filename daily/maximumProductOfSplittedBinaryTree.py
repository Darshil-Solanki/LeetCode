# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sum = []
        def get_sum_dfs(node):
            if not node:
                return 0

            left = get_sum_dfs(node.left)
            right = get_sum_dfs(node.right)
            subtree_sum.extend((left, right))
            return node.val+left+right

        ans = 0
        MOD = 1_000_000_007
        total = get_sum_dfs(root)

        for tot in subtree_sum:
            ans = max(ans, tot*(total-tot))

        return ans%MOD
