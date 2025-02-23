# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(preorder, postorder):
            if not preorder: return None
            if len(preorder)==1:
                return TreeNode(preorder[0])
            node = TreeNode(preorder[0])
            rt_idx = len(postorder)-1
            l_idx = postorder.index(preorder[1])
            r_idx = preorder.index(postorder[rt_idx-1])
            if r_idx==1: r_idx = len(preorder)
            node.left = solve(preorder[1:r_idx], postorder[:l_idx+1])
            node.right = solve(preorder[r_idx:], postorder[l_idx+1:rt_idx])
            return node
        return solve(preorder, postorder)

        # more better way to do same thing
        # if not postorder:
        #     return None
        # val = postorder.pop()
        # node = TreeNode(val)
        # if not postorder:
        #     return node

        # i = postorder.index(preorder[1])
        # node.left = self.constructFromPrePost(preorder[1:i+2], postorder[:i+1])
        # node.right = self.constructFromPrePost(preorder[i+2:], postorder[i+1:])

        # return node
