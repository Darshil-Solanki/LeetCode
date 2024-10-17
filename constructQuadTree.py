"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def isAllSame(self, grid, n):
        temp = grid[0][0]
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=temp:
                    return False
        return True
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def createQuadTree(grid, n):
            node = Node(None, None, None, None, None, None)
            node.val = grid[0][0]
            if self.isAllSame(grid, n):
                node.isLeaf = True 
                return node
            node.isLeaf = False
            tlGrid = [ [ grid[i][j] for j in range(n//2) ] for i in range(n//2)]
            trGrid = [ [ grid[i][j] for j in range(n//2, n) ] for i in range(n//2)]
            blGrid = [ [ grid[i][j] for j in range(n//2) ] for i in range(n//2, n) ]
            brGrid =  [ [ grid[i][j] for j in range(n//2, n) ] for i in range(n//2, n) ]
            node.topLeft = createQuadTree(tlGrid, n//2)
            node.topRight = createQuadTree(trGrid, n//2)
            node.bottomLeft = createQuadTree(blGrid, n//2)
            node.bottomRight = createQuadTree(brGrid, n//2)
            return node 

        return createQuadTree(grid, n)
    
    # Better way don't copy and pass only r and c index make efficient because no need to create multiple copy
    # def construct(self, grid: List[List[int]]) -> 'Node':
    #     def dfs(n,r,c):
    #         allsame =  True 
    #         for i in range(n):
    #             for j in range(n):
    #                 if grid[r][c]!= grid[r+i][c+j]:
    #                     allsame = False 
    #                     break 

    #         if allsame:
    #             return Node(grid[r][c], True)

    #         n = n//2
    #         topleft = dfs(n, r,c)
    #         topright = dfs(n, r, c+n)
    #         bottomleft = dfs(n,r+n, c)
    #         bottomright = dfs(n, r+n, c+n)

    #         return Node(0,False, topleft, topright, bottomleft, bottomright)

    #     return dfs(len(grid), 0,0)
