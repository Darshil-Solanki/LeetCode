class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        matrix = [list(map(int, row)) for row in matrix]

        for i in range(m):
            for j in range(1, n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i][j-1]
                
        ans = 0
        for j in range(n):
            for i in range(m):
                width = matrix[i][j]
                if not width:
                    continue
                
                curr_width = width
                k = i
                while k>-1 and matrix[k][j]:
                    curr_width = min(curr_width, matrix[k][j])
                    height = i - k + 1
                    ans = max(ans, curr_width*height)
                    k -= 1
        
        return ans
