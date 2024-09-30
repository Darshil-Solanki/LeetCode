# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, leftVal=float('-inf'), rightVal=float('inf')):
            left = right = True
            if root.left:
                if root.left.val<=leftVal or root.left.val>=root.val:
                    return False
                left = check(root.left, leftVal, root.val)
            if root.right:
                if root.right.val>=rightVal or root.right.val<=root.val:
                    return False
                right = check(root.right, root.val, rightVal)
            return left and right
        return check(root)
