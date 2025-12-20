class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        columns = [[] for _ in range(n)]
        for row in strs:
            for j, c in enumerate(row):
                columns[j].append(c)
        
        ans = 0
        for i in range(n):
            if columns[i] != sorted(columns[i]):
                ans += 1
        return ans
