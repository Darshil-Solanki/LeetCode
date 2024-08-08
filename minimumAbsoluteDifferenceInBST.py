# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, li):
        if not root:
            return
        elif not root.left and not root.right:
            li.append(root.val)
        else:
            self.traverse(root.left, li)
            self.traverse(root.right, li)
            li.append(root.val)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lTree = []
        self.traverse(root, lTree)
        lTree.sort()
        prev = lTree[0]
        diff = float('inf')
        for i in range(1,len(lTree)):
            diff = lTree[i]-prev if lTree[i]-prev<diff else diff
            prev = lTree[i]
        return diff
