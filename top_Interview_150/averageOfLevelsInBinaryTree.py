# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sumAtLevel, countAtLevel, level):
        if not root:
            return 
        elif not root.left and not root.right:
            if sumAtLevel.get(level) is not None:
                sumAtLevel[level]+=root.val
                countAtLevel[level]+=1
            else:
                sumAtLevel[level]=root.val
                countAtLevel[level]=1
        else:
            self.dfs(root.left, sumAtLevel, countAtLevel, level+1 )
            self.dfs(root.right, sumAtLevel, countAtLevel, level+1)
            if sumAtLevel.get(level) is not None:
                sumAtLevel[level]+=root.val
                countAtLevel[level]+=1
            else:
                sumAtLevel[level]=root.val
                countAtLevel[level]=1

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sumAtLevel, countAtLevel, level = {},{},0
        self.dfs(root, sumAtLevel, countAtLevel, level)
        averages = []
        for i in range(len(sumAtLevel.keys())):
            averages.append(sumAtLevel[i]/countAtLevel[i])
        return averages        
        
