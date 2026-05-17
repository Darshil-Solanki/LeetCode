class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        # copied from contest submission
        n, m = len(matrix), len(matrix[0])

        pref = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(201)]

        for v in range(201):
            p = pref[v]
            for i in range(n):
                row = 0
                for j in range(m):
                    row += matrix[i][j] > v
                    p[i + 1][j + 1] = p[i][j + 1] + row

        ans = 0

        for i in range(n):
            for j in range(m):
                x = matrix[i][j]

                if x == 0:
                    continue

                r1 = max(0, i - x)
                c1 = max(0, j - x)
                r2 = min(n - 1, i + x)
                c2 = min(m - 1, j + x)

                p = pref[x]

                cnt = (
                    p[r2 + 1][c2 + 1]
                    - p[r1][c2 + 1]
                    - p[r2 + 1][c1]
                    + p[r1][c1]
                )

                for dr in (-x, x):
                    for dc in (-x, x):
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > x:
                            cnt -= 1

                if cnt == 0:
                    ans += 1

        return ans
