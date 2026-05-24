class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dfs(i):
            ans = 1
            for j in range(i-1, max(i-d-1, -1), -1):
                if arr[j]>=arr[i]:
                    break
                ans = max(ans, 1+dfs(j))
            
            for j in range(i+1, min(n, i+d+1)):
                if arr[j]>=arr[i]:
                    break
                ans = max(ans, 1+dfs(j))

            return ans
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        
        return ans
