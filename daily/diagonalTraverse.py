class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        inc_diagonal = []
        for i in range(0, m, 2):
            idx, j = i, 0
            temp = []
            while idx>=0 and j<n:
                temp.append(mat[idx][j])
                j += 1
                idx -= 1
            inc_diagonal.append(temp)

        for j in range(2 if m%2 else 1, n, 2):
            i, temp_j = m-1, j
            temp = []
            while i>=0 and temp_j<n:
                temp.append(mat[i][temp_j])
                temp_j += 1
                i -= 1
            inc_diagonal.append(temp)
        
        dec_diagonal = []
        for j in range(1, n, 2):
            i, temp_j = 0, j
            temp = []
            while temp_j>=0 and i<m:
                temp.append(mat[i][temp_j])
                i += 1
                temp_j -= 1
            dec_diagonal.append(temp)
        
        for i in range(1 if n%2 else 2, m, 2):
            idx, j = i, n-1
            temp = []
            while idx<m and j>=0:
                temp.append(mat[idx][j])
                idx += 1
                j -= 1
            dec_diagonal.append(temp)
        
        i_len, d_len = len(inc_diagonal), len(dec_diagonal)
        flag = True
        i, d = 0, 0
        ans = []
        while i<i_len and d<d_len:
            if flag:
                ans.extend(inc_diagonal[i])
                flag = False
                i += 1
            else:
                ans.extend(dec_diagonal[d])
                flag = True
                d += 1
        if i<i_len:
            ans.extend(inc_diagonal[i])
        if d<d_len:
            ans.extend(dec_diagonal[d])

        return ans
