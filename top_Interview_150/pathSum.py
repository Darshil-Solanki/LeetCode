# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, prevtotal: int = 0) -> bool:
        if not root:
            return False
        else:
            if prevtotal+root.val==targetSum and not root.left and not root.right:
                return True
            elif prevtotal+root.val!=targetSum and not root.left and not root.right:
                return False
            else:
                left = self.hasPathSum(root.left, targetSum, prevtotal+root.val)
                right = self.hasPathSum(root.right, targetSum, prevtotal+root.val)
                return left or right 
        
