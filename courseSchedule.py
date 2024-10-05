class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst]+=1
        
        queue = []
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        
        return sum(indegree)==0

        # DFS Way
        # if not prerequisites: return True
        # adj = collections.defaultdict(list)
        # for crs, prs in prerequisites:
        #     adj[crs].append(prs)
        
        # seen = set()
        # def dfs(crs):
        #     if crs in seen:
        #         return False
        #     if not adj[crs]:
        #         return True

        #     seen.add(crs)
        #     for prs in adj[crs]:
        #         if not dfs(prs): return False
        #     seen.remove(crs)

        #     return True

        # for crs in range(numCourses):
        #     if not dfs(crs): return False
        # return True
