# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = defaultdict(int)
        count[0]=1
        def dfs_backtrack(node, currSum):
            if not node:
                return
            currSum+=node.val
            self.ans+=count[currSum-targetSum]
            count[currSum]+=1

            dfs_backtrack(node.left, currSum)
            dfs_backtrack(node.right, currSum)

            count[currSum]-=1

        dfs_backtrack(root, 0)
        return self.ans

        # O(n^2)
        # def dfs_pathcount(node, currSum):
        #     if not node:
        #         return 0
        #     currSum+=node.val
        #     if currSum==targetSum:
        #         self.ans+=1
        #     dfs_pathcount(node.left, currSum)
        #     dfs_pathcount(node.right, currSum)

        # def dfs_move(node):
        #     if not node:
        #         return
        #     dfs_pathcount(node, 0)
        #     dfs_move(node.left)
        #     dfs_move(node.right)
        # dfs_move(root)

        # return self.ans
