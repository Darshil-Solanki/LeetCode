# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if inorder:
                root = TreeNode(preorder.pop(0))
                idx = inorder.index(root.val)
                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])
                return root
        return build(preorder, inorder)

        # Better Solution using mapping to time complexity to find index
        # mapping = {}

        # for i in range(len(inorder)):
        #     mapping[inorder[i]] = i
        
        # preorder = collections.deque(preorder)

        # def build(start, end):
        #     if start > end: return None

        #     root = TreeNode(preorder.popleft())
        #     mid = mapping[root.val]

        #     root.left = build(start, mid - 1)
        #     root.right = build(mid + 1, end)

        #     return root

        # return build(0, len(preorder) - 1)
