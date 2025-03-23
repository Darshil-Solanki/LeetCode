class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a, b):
            a = set(a)
            b = set(b)
            return len(a&b)

        graph = defaultdict(list)
        n = len(properties)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if intersect(properties[i], properties[j])>=k:
                        graph[i].append(j)
                        graph[j].append(i)

        def dfs(i):
            visited[i]=True
            for nei in graph[i]:
                if not visited[nei]:
                    dfs(nei)

        ans = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans+=1

        return ans

        # find and union faster approach taken from submission
        # n = len(properties)
        # p = list(range(n))
        # def find(x):
        #     if p[x] != x: p[x] = find(p[x])
        #     return p[x]
        # s = [set(x) for x in properties]
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if len(s[i] & s[j]) >= k:
        #             p[find(j)] = find(i)
        # return len({find(x) for x in range(n)})
