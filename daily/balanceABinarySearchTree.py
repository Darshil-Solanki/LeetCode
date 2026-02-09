# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            values.append(node.val)
            if node.right:
                dfs(node.right)
            return
        
        dfs(root)

        
        def create_tree(start, end):
            if start>end:
                return None
            
            mid = (start+end)//2
            left_subtree = create_tree(start, mid-1)
            right_subtree = create_tree(mid+1, end)
            node = TreeNode(values[mid], left_subtree, right_subtree)
            return node
            
        
        return create_tree(0, len(values)-1)
