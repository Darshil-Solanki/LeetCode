class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        ans = 0
        n = len(nums)
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        def is_connected_even(curr_set):
            self.tot = 0
            if not curr_set:
                return 0
            connections = {c:False for c in curr_set}
            def dfs(u):
                if u not in curr_set:
                    return
                self.tot += nums[u]
                connections[u] = True
                for nei in graph[u]:
                    if nei in curr_set and not connections[nei]:
                        dfs(nei)

            start = curr_set.pop()
            curr_set.add(start)
            tot = dfs(start)
            return int(all(connections[c] for c in curr_set) and self.tot%2==0)
            
        def dp(i, curr_set):
            if i == n:
                return is_connected_even(curr_set)
                
            curr_set.add(i)
            keep = dp(i+1, curr_set)
            
            curr_set.remove(i)
            not_keep = dp(i+1, curr_set)

            return keep + not_keep
            
        return dp(0, set())
                
