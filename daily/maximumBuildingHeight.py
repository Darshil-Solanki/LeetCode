class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Copied from submissions
        rest = restrictions
        rest.append([1, 0])
        rest.sort()
        
        if rest[-1][0] != n:
            rest.append([n, n-1])
        
        m = len(rest)
        
        for i in range(1, m):
            rest[i][1] = min(rest[i][1], rest[i-1][1] + (rest[i][0] - rest[i-1][0]))
        
        for i in range(m-2, 0, -1):
            rest[i][1] = min(rest[i][1], rest[i+1][1] + (rest[i+1][0] - rest[i][0]))
        
        ans = 0
        for i in range(m-1):
            best = ((rest[i+1][0] - rest[i][0]) + rest[i][1] + rest[i+1][1] ) // 2
            if best>ans:
                ans = best
        
        return ans
