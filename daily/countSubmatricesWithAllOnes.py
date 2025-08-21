class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if j>0:
                        mat[i][j] = mat[i][j-1]+1

                    curr = mat[i][j]
                    for k in range(i, -1, -1):
                        curr = min(curr, mat[k][j])
                        if not curr:
                            break
                        ans += curr
        
        return ans
