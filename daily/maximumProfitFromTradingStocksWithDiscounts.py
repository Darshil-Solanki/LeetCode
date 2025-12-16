class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = defaultdict(list)

        for u, v in hierarchy:
            graph[u-1].append(v-1)

        def dfs(u):
            cost = present[u]
            d_cost = present[u]//2

            dp0 = [0]*(budget+1) # non discount
            dp1 = [0]*(budget+1) # discounted

            sub_profit0 = [0]*(budget+1)
            sub_profit1 = [0]*(budget+1)
            
            u_size = cost
            for v in graph[u]:
                child_dp0, child_dp1, v_size = dfs(v)
                u_size += v_size
                for i in range(budget, -1, -1):
                    for sub in range(min(v_size, i)+1):
                        if i-sub>=0:
                            sub_profit0[i] = max(sub_profit0[i], sub_profit0[i-sub]+child_dp0[sub])
                            sub_profit1[i] = max(sub_profit1[i], sub_profit1[i-sub]+child_dp1[sub])
            
            for i in range(budget+1):
                dp0[i] = sub_profit0[i]
                dp1[i] = sub_profit0[i]
                if i>=d_cost:
                    dp1[i] = max(sub_profit0[i], sub_profit1[i-d_cost]+future[u]-d_cost)
                if i>=cost:
                    dp0[i] = max(sub_profit0[i], sub_profit1[i-cost]+future[u]-cost)
            return dp0, dp1, u_size
        
        return dfs(0)[0][budget]
