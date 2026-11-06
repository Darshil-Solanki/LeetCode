class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x: x[1])
        new_queries = list(enumerate(queries))
        new_queries.sort(key = lambda x: x[1])

        ans = [0] * len(queries)
        cnt = Counter()
        left = right = active = 0
        for o_idx, right_t in new_queries:
            while right < len(logs) and logs[right][1] <= right_t:
                s_id = logs[right][0]
                if cnt[s_id] == 0:
                    active += 1
                cnt[s_id] += 1
                right += 1
            
            while left < right and logs[left][1] < right_t - x:
                s_id = logs[left][0]
                cnt[s_id] -= 1
                if cnt[s_id] == 0:
                    active -= 1
                left += 1

            ans[o_idx] = n - active
        
        return ans
