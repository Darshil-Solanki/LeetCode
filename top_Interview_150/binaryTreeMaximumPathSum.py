# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res=max(self.res, node.val+left+right, node.val, node.val+left, node.val+right)
            return max(node.val, node.val+left,node.val+right)
        dfs(root)
        return self.res

    # Bit Better Solution from submission
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     self.maxSum = float('-inf')
        
    #     def dfs(node: Optional[TreeNode]) -> int:
    #         if not node: return 0
            
    #         leftGain = dfs(node.left)
    #         if leftGain < 0: leftGain = 0

    #         rightGain = dfs(node.right)
    #         if rightGain < 0: rightGain = 0
            
    #         curSum = leftGain + rightGain + node.val
    #         if curSum > self.maxSum: self.maxSum = curSum
    #         if leftGain > rightGain: return leftGain + node.val
            
    #         return rightGain + node.val
    #     dfs(root)
    #     return self.maxSum
