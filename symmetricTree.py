# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.isMirror(root.left, root.right)

# Improve version from online

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True 
#         queue=[root.left,root.right]
#         while queue:
#             left=queue.pop(0)
#             right=queue.pop(0)
#             #print(right.val)
#             if not left and not right :
#                 continue
#             if not left or not right:
#                 return False
#             if left.val!=right.val:
#                 return False
#             queue.extend([left.left,right.right])
#             queue.extend([left.right,right.left])
#         return True 
