# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self,root: [TreeNode]) -> int:
        h = 0
        while root:
            root = root.left
            h+=1
        return h

    def nodeExist(self, index, height, right, root):
        left = 0
        for _ in range(height-1):
            mid = (left+right)//2
            if index<=mid:
                right=mid
                root=root.left
            else:
                left=mid+1
                root=root.right
        return root is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        height = self.getHeight(root)
        if not height:
            return 0
        maxNode = (1<<(height-1))-1
        left, right  = 0, maxNode
        while left<=right:
            mid = (left+right)//2
            if self.nodeExist(mid, height, maxNode, root):
                left=mid+1
            else:
                right=mid-1

        return (1<<(height-1))+right
	# O(n) solution
    # def countNodes(self, root: Optional[TreeNode])->int:
    #     if not root:
    #         return 0
    #     elif not root.left and not root.right:
    #         return 1
    #     else:
    #         return self.countNodes(root.left)+self.countNodes(root.right)+1 
