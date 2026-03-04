class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_one_cnt = [0]*m
        col_one_cnt = [0]*n
        for i, row in enumerate(mat):
            row_one_cnt[i] = row.count(1)
            for j, num in enumerate(row):
                if num:
                    col_one_cnt[j] += 1
        
        ans = 0
        for i in range(m):
            if row_one_cnt[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1:
                        if col_one_cnt[j]==1:
                            ans += 1
                        break
        return ans

        # better solution for python
        # @cache
        # def get_column_sum(col_idx):
        #     return sum(row[col_idx] for row in mat)

        # special = 0
        # for row in mat:
        #     if sum(row) == 1:
        #         col_idx = row.index(1)
        #         special += get_column_sum(col_idx) == 1

        # return special
