class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(nums)
        self.ans = float("inf")

        total = 0
        for val in nums:
            total ^= val
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def calc(p1, p2, p3):
            return max(p1, p2, p3)-min(p1, p2, p3)

        def dfs2(node, parent, xor, anc):
            val = nums[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                val ^= dfs2(nei, node, xor, anc)
            
            if parent==anc:
                return val
            
            self.ans = min(self.ans, calc(xor, val, total^xor^val))
            return val

        
        def dfs(node, parent):
            val = nums[node]
            for nei in graph[node]:
                if nei==parent:
                    continue
                val ^= dfs(nei, node)

            for nei in graph[node]:
                if nei==parent:
                    dfs2(nei, node, val, node)
            return val
        
        dfs(0, -1)
        return self.ans
