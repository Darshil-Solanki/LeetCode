# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def backtrack_gen(left, right):
            if left>right: return [None]

            ans = []
            for val in range(left, right+1):
                for left_tree in backtrack_gen(left, val-1):
                    for right_tree in backtrack_gen(val+1, right):
                        root = TreeNode(val, left_tree, right_tree)
                        ans.append(root)
            
            return ans

        return backtrack_gen(1, n)
