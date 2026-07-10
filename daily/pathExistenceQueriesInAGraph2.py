class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # copied from solutions
        sorted_nums = [(num, i) for i, num in enumerate(nums)]
        sorted_nums.sort()
        curr_idx = [0]*n
        for i, (_, orig_idx) in enumerate(sorted_nums):
            curr_idx[orig_idx] = i
        
        LOG = 18
        st = [[0] * LOG for _ in range(n)]

        r = 0
        for i in range(n):
            if r<i:
                r = i
            while (r + 1 < n and sorted_nums[r+1][0] - sorted_nums[r][0] <= maxDiff and 
                    sorted_nums[r+1][0] - sorted_nums[i][0] <= maxDiff
                    ):
                r += 1
            st[i][0] = r
        
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j-1]][j-1]
        
        ans = []
        for u, v in queries:
            a, b = curr_idx[u], curr_idx[v]
            if a>b: a, b = b, a
            if a == b:
                ans.append(0)
                continue
            
            curr, steps = a, 0
            for j in range(LOG-1, -1, -1):
                if st[curr][j]<b:
                    curr = st[curr][j]
                    steps += (1<<j)
            
            ans.append(steps + 1 if st[curr][0] >= b else -1)
        
        return ans
