class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available_heap = [(s, i) for i, s in enumerate(servers)]
        heapify(available_heap)

        working_heap = []

        def release():
            while working_heap and working_heap[0][0] <= t:
                _, idx = heappop(working_heap)
                heappush(available_heap, (servers[idx], idx))

        t = 0
        ans = []
        for i, task in enumerate(tasks):
            t = max(t, i)
            release()
            if not available_heap:
                t = working_heap[0][0]
                release()
            
            _, idx = heappop(available_heap)
            ans.append(idx)
            heappush(working_heap, (t+task, idx))
        
        return ans
