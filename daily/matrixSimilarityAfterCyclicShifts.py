class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        if not k:
            return True
        temp = [row[:] for row in mat]
        for _ in range(k):
            for i, row in enumerate(temp):
                if i%2:#odd
                    row.insert(0, row.pop())
                else: #even
                    row.append(row.pop(0))
            if temp == mat:
                return True
        return False
    
    # m.n time complexity checking inverse which can't be at this place
    # def areSimilar(self, mat: List[List[int]], k: int) -> bool:
    #     n, m = len(mat), len(mat[0])

    #     for i in range(n):
    #         for j in range(m):
    #             if mat[i][(j + (k if i % 2 == 0 else -k)) % m] != mat[i][j]:
    #                 return False
    #     return True
