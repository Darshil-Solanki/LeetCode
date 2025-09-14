class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float("inf")
        for s, e in tasks:
            ans = min(ans, s+e)
        return ans            
