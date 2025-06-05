class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = [[] for _ in range(26)]

        for a, b in zip(s1, s2):
            u, v = ord(a)-97, ord(b)-97
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0]*26
        min_char = [25]*26
        for c in range(26):
            if not visited[c]:
                ans = c
                queue = deque([c])
                visited[c] = 1
                group = []

                while queue:
                    node = queue.popleft()
                    group.append(node)
                     
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = 1
                            queue.append(nei)
                
                min_c = min(group) if group else 25
                for c in group:
                    min_char[c] = min_c
                
        
        result = []
        for c in baseStr:
            result.append(chr(min_char[ord(c)-97]+97))
        
        return "".join(result)
