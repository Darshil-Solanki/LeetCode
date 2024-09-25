# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        flag = True
        ans = []
        queue = [root]
        while queue:
            curr_len = len(queue)
            temp = []
            for i in range(curr_len):
                node = queue.pop(0)
                if flag:
                    temp.append(node.val)
                else:
                    temp.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = not flag
            ans.append(temp)
        return ans 
