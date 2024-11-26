class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return list(range(numCourses))

        outdegree = [0]*numCourses
        adjList = collections.defaultdict(list)
        for crs, prs in prerequisites:
            adjList[prs].append(crs)
            outdegree[crs]+=1
        
        queue = []
        for i in range(numCourses):
            if outdegree[i]==0:
                queue.append(i)
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            for nei in adjList[node]:
                outdegree[nei]-=1
                if outdegree[nei]==0:
                    queue.append(nei)
                
        if len(res)==numCourses:
            return res
        return []

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution().findOrder(nums, next(inputs))).replace(" ", ""), file=f)
exit(0)
