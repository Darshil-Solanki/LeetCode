# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def getSum(root, curr):
            if not root.left and not root.right:
                return curr*10+root.val
            ans = curr*10+root.val
            left = right = 0
            if root.left:
                left = getSum(root.left, ans)
            if root.right:
                right = getSum(root.right, ans)
            return left+right
        return getSum(root,0)
            
