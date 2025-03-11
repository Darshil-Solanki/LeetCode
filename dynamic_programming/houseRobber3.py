# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node, can_rob):
            if not node: return 0
            if (node, can_rob) in memo: return memo[(node, can_rob)]

            loot = dont_loot = 0
            if can_rob:
                loot = max(node.val+dp(node.left, 0)+dp(node.right, 0), dp(node.left, 1)+dp(node.right, 1))
            else:
                dont_loot = dp(node.left, 1)+dp(node.right, 1)

            ans = max(loot, dont_loot)
            memo[(node, can_rob)] = ans

            return ans

        memo = {}
        return max(dp(root, 1), dp(root, 0))
    
    # Faster better approach without need of memoization only traversing node at one time
    # def rob(self, root: TreeNode) -> int:
        
    #     def rob_helper(node):
    #         if not node:
    #             return 0, 0

    #         rob_left, not_rob_left = rob_helper(node.left)
    #         rob_right, not_rob_right = rob_helper(node.right)

    #         rob_node = node.val + not_rob_left + not_rob_right
    #         not_rob_node = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)

    #         return rob_node, not_rob_node

    #     rob, not_rob = rob_helper(root)
    #     return max(rob, not_rob)
