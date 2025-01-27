class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(numCourses)]
        
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(u, v):
            ans = False
            for nei in graph[u]:
                if nei not in seen:
                    if nei==v: return True
                    seen.add(nei)
                    ans = ans or dfs(nei, v)
            return ans
        
        res = []
        for u, v in queries:
            seen = {u}
            res.append(dfs(u, v))
        return res

        # faster method from submission precompute transitive courses 
        # graph = defaultdict(list)
        # for prereq, postreq in prerequisites:
        #     graph[prereq].append(postreq)

        # postreq_set = [set() for _ in range(numCourses)]
    
        # def dfs(course):
        #     for postreq in graph[course]:
        #         if postreq not in postreq_set[course]:
        #             postreq_set[course].add(postreq)
        #             postreq_set[course].update(dfs(postreq))
        #     return postreq_set[course]
            
        # for i in range(numCourses):
        #     dfs(i)
        
        # res = []
        # for prereq, postreq in queries:
        #     if postreq not in postreq_set[prereq]:
        #         res.append(False)
        #     else:
        #         res.append(True)
        # return res
