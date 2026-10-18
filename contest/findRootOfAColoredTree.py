class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        tree = defaultdict(list)
        n = len(colors)
        next_color = {"R":"B", "B":"W", "W":"R"}
        indegree = [0]*n
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            if next_color[colors[u]] == colors[v]:
                indegree[v] += 1
            elif next_color[colors[v]] == colors[u]:
                indegree[u] += 1
            else:
                return -1

        roots = [i for i in range(n) if indegree[i] == 0]
        if len(roots) != 1:
            return -1

        root = roots[0]
        if len(tree[root]) > 2:
            return -1

        return root
