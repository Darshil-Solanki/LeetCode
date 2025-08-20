class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            matrix[i].append(0)
        matrix.append([0]*(n+1))

        ans = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])+1
                    ans += matrix[i][j]
        
        return ans
