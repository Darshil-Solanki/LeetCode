class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        self.ans = 0
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)

        def dfs(node):
            if not node in tree: return cost[node]

            path_sum_amount = []
            for child in tree[node]:
                path_sum_amount.append(dfs(child))

            mx_amount = max(path_sum_amount)
            self.ans += sum(amount!=mx_amount for amount in path_sum_amount)

            return mx_amount+cost[node]
            
        
        dfs(0)
        return self.ans
