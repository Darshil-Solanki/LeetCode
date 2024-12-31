# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, maxNum):
            if not root: return
            if root.val>=maxNum:
                self.ans+=1
                maxNum=root.val
            dfs(root.left, maxNum)
            dfs(root.right, maxNum)
        dfs(root, float("-inf"))
        return self.ans
        
