# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        i = 1
        root = TreeNode(int(traversal[0]))
        stack = [root]
        while i<n:
            count = 0
            while traversal[i]=="-":
                count+=1
                i+=1
            value = 0
            while i<n and traversal[i].isdigit():
                value = value*10+int(traversal[i])
                i+=1
            node = TreeNode(value)
            while len(stack)>count:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return root
