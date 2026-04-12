class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        ans = [0]*n
        for i, row in enumerate(matrix):
            for j, is_connected in enumerate(row):
                if is_connected:
                    ans[i] += 1
                    ans[j] += 1
        return [d//2 for d in ans]
