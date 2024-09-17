# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map = {}
        for idx,val in enumerate(inorder):
            map[val]=idx
        
        def build(start, end):
            if start>end:return None
            root = TreeNode(postorder.pop())
            mid = map[root.val]
            root.right = build(mid+1, end)
            root.left = build(start, mid-1)

            return root
        
        return build(0, len(inorder)-1)
