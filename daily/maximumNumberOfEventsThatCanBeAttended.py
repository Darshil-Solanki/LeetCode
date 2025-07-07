class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        max_day = max(event[1] for event in events)
        ans = 0
        heap = []
        i = 0

        for day in range(1, max_day+1):
            while i<n and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1
            
            while heap and heap[0]<day:
                heappop(heap)
            
            if heap:
                heappop(heap)
                ans += 1
        
        return ans
