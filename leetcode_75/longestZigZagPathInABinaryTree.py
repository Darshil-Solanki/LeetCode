# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, pathSum, flag):
            if not node:
                return pathSum
            l = r = 0
            if flag:
                l = dfs(node.left, pathSum+1, False)
                r = dfs(node.right, 1, True)
            else:
                l = dfs(node.left, 1, False)
                r = dfs(node.right, pathSum+1, True)
            return max(l, r) 

        return max(dfs(root, 0, True), dfs(root, 0, False))-1

        # Better efficient Approach 
        # max_path = -1
        # def dfs(node, curr_path_len, parent_direction):
        #     nonlocal max_path
        #     if curr_path_len > max_path:
        #         max_path = curr_path_len
        #     if node.left:
        #         if parent_direction:
        #             dfs(node.left, curr_path_len + 1, False)
        #         else:
        #             dfs(node.left, 1, False)
        #     if node.right:
        #         if not parent_direction:
        #             dfs(node.right, curr_path_len + 1, True)
        #         else:
        #             dfs(node.right, 1, True)
        # dfs(root, 0, True)
        # return max_path
