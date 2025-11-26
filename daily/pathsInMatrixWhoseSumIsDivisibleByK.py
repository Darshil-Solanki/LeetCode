class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])

        prev = [[0]*k for _ in range(n+1)]
        curr = [[0]*k for _ in range(n+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i==1 and j==1:
                    curr[j][grid[0][0]%k] = 1
                    continue

                value = grid[i-1][j-1]%k
                for r in range(k):
                    prev_mod = (r-value+k) % k
                    curr[j][r] = (prev[j][prev_mod] + curr[j-1][prev_mod]) % MOD
                    
            prev, curr = curr, prev
        
        return prev[n][0]
