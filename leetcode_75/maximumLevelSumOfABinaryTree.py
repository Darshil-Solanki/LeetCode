# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        level, currlevel = 0, 0
        queue = deque([root])
        while queue:
            tempSum = 0
            currlevel += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                tempSum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if tempSum>maxSum: 
                maxSum = tempSum
                level = currlevel
        return level       
