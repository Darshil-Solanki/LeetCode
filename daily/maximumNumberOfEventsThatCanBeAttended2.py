class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [st for st, _, _ in events]
        dp = [[-1]*n for _ in range(k+1)]

        def dfs(curr_idx, remaining):
            if remaining == 0 or curr_idx == n:
                return 0

            if dp[remaining][curr_idx] != -1:
                return dp[remaining][curr_idx]

            next_idx = bisect_right(starts, events[curr_idx][1])
            not_attended = dfs(curr_idx+1, remaining)
            attended = events[curr_idx][2]+dfs(next_idx, remaining-1)
            ans = max(attended, not_attended)
            dp[remaining][curr_idx] = ans

            return ans  

        return dfs(0, k)
