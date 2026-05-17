class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        n = len(arr)
        visited = [False]*n

        while queue:
            i = queue.popleft()
            visited[i] = True
            if arr[i] == 0:
                return True
            if i-arr[i]>-1 and not visited[i-arr[i]]:
                queue.append(i-arr[i])
            if i+arr[i]<n and not visited[i+arr[i]]:
                queue.append(i+arr[i])
        
        return False
