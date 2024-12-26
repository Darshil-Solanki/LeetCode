class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        rowHash, columnHash = defaultdict(int), defaultdict(int)
        for i, row in enumerate(grid):
            rowHash["_".join(map(str, row))] += 1
        for i in range(n):
            temp = ""
            for j in range(n):
                temp+=(str(grid[j][i])+("_" if j!=n-1 else ""))
            columnHash[temp] += 1
        for k, v in rowHash.items():
            if k in columnHash:
                ans+=columnHash[k]*v
        return ans

        # faster solution
        # rows = Counter(tuple(i) for i in grid)
        # cols = list(zip(*grid))
        # return sum([rows[i] for i in cols])
