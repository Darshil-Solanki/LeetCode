class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0]*n for _ in range(m)]
        candidates = defaultdict(list)
        
        for j, cell in enumerate(mat[0]):
            if cell:
                candidates[1].append((0, j))
            dp[0][j] = cell
        for i in range(m):
            dp[i][0] = mat[i][0]
            if dp[i][0] and i:
                candidates[1].append((i, 0))

        for i in range(1, m):
            for j in range(1, n):
                size = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1 if mat[i][j] else 0
                dp[i][j] = size
                if size:
                    candidates[size].append((i, j))
        
        def check(k):
            square_list = candidates[k]
            if len(square_list)<2:
                return False

            for ai, aj in square_list:
                for bi, bj in square_list:
                    if ((ai-k+1 <= bi-k+1 <= ai) or (ai-k+1 <= bi <= ai)) and ((aj-k+1 <= bj-k+1 <= aj) or (aj-k+1 <= bj <= aj)):
                        continue
                    return True
                    
        for k in sorted(candidates.keys(), reverse=True):
            if check(k):
                return k*k
        return 0        
