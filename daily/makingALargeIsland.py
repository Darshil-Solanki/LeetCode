class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(i, j):
            ans=0
            if (i, j) in seen: return 0
            seen.add((i, j))
            if grid[i][j]:
                ans=1
                group_map[(i, j)]=group
                if 0<i: ans+=dfs(i-1, j)
                if i<n-1: ans+=dfs(i+1, j)
                if 0<j: ans+=dfs(i, j-1)
                if j<n-1: ans+=dfs(i, j+1)
            return ans
                
        size_map = defaultdict(int)
        group_map = defaultdict(int)
        seen = set()
        group = 0
        zeroLoc = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if not cell:
                    zeroLoc.append((i,j))
                if (i, j) not in seen:
                    group+=1
                    size_map[group]=dfs(i,j)
        if not zeroLoc: return n*n
        if len(zeroLoc)==n*n: return 1
        maxSize = max(size_map.values())+1
        for i, j in zeroLoc:
            size, group = [0]*4, [0]*4
            if i>0:
                group[0] = group_map[(i-1, j)]
                size[0] = size_map[group[0]]
            if i<n-1:
                if group_map[(i+1, j)] not in group:
                    group[3] = group_map[(i+1, j)]
                size[3] = size_map[group[3]]
            if j>0: 
                if group_map[(i, j-1)] not in group:
                    group[1] = group_map[(i, j-1)]
                size[1] = size_map[group[1]]
            if j<n-1: 
                if group_map[(i, j+1)] not in group:
                    group[2] = group_map[(i, j+1)]
                size[2] = size_map[group[2]]
            if sum(size)+1>maxSize: maxSize=sum(size)+1 

        return maxSize

        # faster method
        # n = len(grid)
        # id = 2
        # sz = {}

        # def dfs(row, col, isl_id):
        #     grid[row][col] = isl_id
        #     size = 1

        #     if row != 0:
        #         if grid[row - 1][col] == 1:
        #             size += dfs(row - 1, col, isl_id)
        #     if col != 0:
        #         if grid[row][col - 1] == 1:
        #             size += dfs(row, col - 1, isl_id)
        #     if row != n - 1:
        #         if grid[row + 1][col] == 1:
        #             size += dfs(row + 1, col, isl_id)
        #     if col != n - 1:
        #         if grid[row][col + 1] == 1:
        #             size += dfs(row, col + 1, isl_id)
            
        #     return size
        
        # for i in range(n):
        #     for j in range(n):
        #         ts = 0
        #         if grid[i][j] == 1:
        #             ts = dfs(i, j, id)
        #             sz[id] = ts
        #             id += 1
        
        # if not sz:
        #     return 1
        
        # res = max(sz.values())

        # for i in range(n):
        #     for j in range(n):
                
        #         if grid[i][j] == 0:
        #             sn = set()
        #             p = 1

        #             if i != 0:
        #                 if grid[i - 1][j] > 1:
        #                     t = grid[i - 1][j]
        #                     if t not in sn:
        #                         p += sz[t]
        #                         sn.add(t)
                    
        #             if i != n - 1:
        #                 if grid[i + 1][j] > 1:
        #                     t = grid[i + 1][j]
        #                     if t not in sn:
        #                         p += sz[t]
        #                         sn.add(t)
                    
        #             if j != 0:
        #                 if grid[i][j - 1] > 1:
        #                     t = grid[i][j - 1]
        #                     if t not in sn:
        #                         p += sz[t]
        #                         sn.add(t)
                    
        #             if j != n - 1:
        #                 if grid[i][j + 1] > 1:
        #                     t = grid[i][j + 1]
        #                     if t not in sn:
        #                         p += sz[t]
        #                         sn.add(t)
                    
        #             res = max(res, p)
        # return res
