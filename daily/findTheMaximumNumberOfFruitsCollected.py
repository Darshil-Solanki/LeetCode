class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        tot = 0
        n = len(fruits)
        # First Kid will always go in diagonal
        for i in range(n):
            tot += fruits[i][i]
            fruits[i][i] = 0
        
        # child 2
        @cache
        def dfs(i, j):
            if i==n-1 and j==n-1:
                temp = fruits[i][j]
                fruits[i][j] = 0
                return temp
            
            left = 0 if j-1<=i+1 else dfs(i+1, j-1)
            bottom = 0 if j<=i+1 else dfs(i+1, j)
            right = 0 if j+1 == n else dfs(i+1, j+1)
            return fruits[i][j] + max(left, bottom, right)
        
        tot += dfs(0, n-1)

        #child3
        @cache
        def dfs(i, j):
            top = 0 if j+1>=i-1 else dfs(i-1, j+1)
            side_by = 0 if j+1>=i else dfs(i, j+1)
            bottom = 0 if i+1 == n else dfs(i+1, j+1)
            return fruits[i][j] + max(top, side_by, bottom)

        tot += dfs(n-1, 0)
        
        return tot
