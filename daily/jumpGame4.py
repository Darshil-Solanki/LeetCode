class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n<2:
            return 0
        
        indices = defaultdict(list)
        for i, num in enumerate(arr):
            indices[num].append(i)
        
        queue = set([0])
        visited = {0}
        step = 0

        while queue:
            next = []
            for i in queue:
                if i == n-1:
                    return step
                for j in indices[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        next.append(j)
                
                indices[arr[i]].clear()

                if i-1>-1 and i-1 not in visited:
                    visited.add(i-1)
                    next.append(i-1)
                if i+1<n and i+1 not in visited:
                    visited.add(i+1)
                    next.append(i+1)
            queue = next
            step += 1
        
        return -1
        
        # def dp(i):
        #     if i == n-1:
        #         return 0
        #     visited[i] = True
        #     left = 1+dp(i-1) if i-1>-1 and not visited[i-1] else float("inf")
        #     right = 1+dp(i+1) if i+1<n and not visited[i+1] else float("inf")
        #     same_num = float("inf")
        #     for j in indices[arr[i]]:
        #         if not visited[j]:
        #             same_num = min(same_num, 1+dp(j))
        #     visited[i] = False
        #     return min(left, right, same_num)

        # visited = [False]*n
        # return dp(0)
