# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count, self.res = 0, -1
        def dfs(node):
            if not node:
                return -1
            dfs(node.left)
            self.count+=1
            if self.count==k:
                self.res = node.val
            dfs(node.right)
        
        dfs(root)
        return self.res

        # Iterative Approach
        # count = 0
        # curr = root
        # stack = []

        # while stack or curr:

        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()
        #     count += 1

        #     if count == k:
        #         return curr.val
            
        #     curr = curr.right

        # return -1
