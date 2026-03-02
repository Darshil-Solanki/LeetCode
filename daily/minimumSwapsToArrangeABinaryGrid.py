class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        one_pos = [-1]*n
        for i, row in enumerate(grid):
            for j in range(n-1, -1, -1):
                if row[j]:
                    one_pos[i] = j
                    break
        
        ans = 0
        for i in range(n):
            k = -1
            for j in range(i, n):
                if one_pos[j]<=i:
                    ans += j-i
                    k = j
                    break
            if k != -1:
                for j in range(k, i, -1):
                    one_pos[j], one_pos[j-1] = one_pos[j-1], one_pos[j]
            else:
                return -1
        
        return ans
